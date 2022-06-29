# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from multiprocessing.spawn import import_main_path
from time import sleep

from google.protobuf.json_format import MessageToDict
from ansible.module_utils.basic import AnsibleModule
from yandexcloud import SDK, RetryInterceptor
from yandex.cloud.resourcemanager.v1.cloud_pb2 import Cloud
from yandex.cloud.resourcemanager.v1.cloud_service_pb2 import ListCloudsRequest
from yandex.cloud.resourcemanager.v1.cloud_service_pb2_grpc import CloudServiceStub
from yandex.cloud.resourcemanager.v1.folder_pb2 import Folder
from yandex.cloud.resourcemanager.v1.folder_service_pb2_grpc import FolderServiceStub
from yandex.cloud.resourcemanager.v1.folder_service_pb2 import ListFoldersRequest


def yc_argument_spec():
    return dict(
        auth=dict(type='dict', options=dict(
            token=dict(type="str", required=False, default=None),
            service_account_key=dict(type="dict", required=False, default=None),
            endpoint=dict(type="str", required=False, default='api.cloud.yandex.net'),
            root_certificates=dict(type="str", required=False, default=None))),
            cloud=dict(type="str", required=False),
            folder=dict(type="str", required=False),
            folder_id=dict(type="str", required=False),
)


class YC(AnsibleModule):
    def __init__(self, *args, **kwargs):
        argument_spec = yc_argument_spec()
        argument_spec.update(kwargs.get("argument_spec", dict()))
        kwargs["argument_spec"] = argument_spec
        super().__init__(*args, **kwargs)
        if not (self.params["auth"]["token"] or self.params["auth"]["service_account_key"]):
            self.fail_json(msg="authorization token or service account key should be provided.")
        interceptor = RetryInterceptor(max_retry_count=10)
        if self.params["auth"]["root_certificates"]:
            self.params["auth"]["root_certificates"] = self.params["auth"]["root_certificates"].encode("utf-8")
        self.sdk = SDK(interceptor=interceptor, **self.params["auth"])
        self.cloud_service = self.sdk.client(CloudServiceStub)
        self.folder_service = self.sdk.client(FolderServiceStub)

    def waiter(self, operation):
        waiter = self.sdk.waiter(operation.id)
        for _ in waiter:
            sleep(1)
        return waiter.operation

    def _list_clouds_by(self, name=None, id=None):
        filter = None
        if not id is None:
            filter = 'id="%s"' % id
        elif not name is None:
            filter = 'name="%s"' % name
        msg = self.cloud_service.List(
            ListCloudsRequest(filter=filter)
        )
        return MessageToDict(msg)

    def _list_folders_by(self, name=None, cloud=None, id=None):
        cloud_ids = []
        filter = None
        result = []
        if not cloud is None:
            cloud_rec = self._list_clouds_by(name=cloud)
            if not cloud_rec:
                raise ValueError(f"Cloud with name:{cloud} not found")
            cloud_ids.append(cloud_rec.get("clouds")[0].get("id"))
        else:
            cloud_rec = self._list_clouds_by()
            if not cloud_rec:
                raise ValueError(f"No clouds found")
            for c in cloud_rec.get("clouds"):
                cloud_ids.append(c.get("id"))
        for cloud_id in cloud_ids:
            if not name is None:
                filter='name="%s"' % name
            folders = self.folder_service.List(
                ListFoldersRequest(cloud_id=cloud_id, filter=filter)
            )
            f = MessageToDict(folders)
            if f:
                return f
        return None


def response_error_check(response):
    if "response" not in response or response["response"].get("error"):
        response["failed"] = True
        response["changed"] = False
    else:
        response["changed"] = True
    return response
