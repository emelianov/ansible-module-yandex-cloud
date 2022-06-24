# ansible-module-yandex-cloud

## Overview

*ansible-module-yandex-cloud* is a set of ansible modules that manage a yandex cloud.

Examples are available as [separete repository](https://github.com/emelianov/ansible-module-yandex-cloud-cookbook).

### Build & Run

### Prerequisites

* The <https://github.com/yandex-cloud/python-sdk> module is required.

1. pip install --user `git+https://github.com/yandex-cloud/python-sdk`
2. git clone `https://github.com/emelianov/ansible-module-yandex-cloud`
3. cd ansible-module-yandex-cloud

## Documentation

### VM managment

```raw
ycc_vm:
        Ansible module to manage (create/update/delete) virtial machines in Yandex compute cloud

  * This module is maintained by The Ansible Community
OPTIONS (= is mandatory):

- assign_public_ip
        Assign public address.
        [Default: False]
        type: bool

- core_fraction
        Guaranteed vCPU share
        [Default: 100]
        choises:
        - 5
        - 20
        - 50
        - 100

        type: int

- cores
        vCPU number.
        [Default: 2]
        type: int

- disk_size
        Primary disk size in GB.
        [Default: 10]
        type: int

- disk_type
        Primary disk type.
        [Default: hdd]
        choises: hdd, nvme
        type: str

= folder_id
        Virtual machine target folder id.

        type: str

- hostname
        Virtual machine hostname, default same as name.
        [Default: (null)]
        type: str

- image_id
        Boot image id.
        Required with `state=present'.
        [Default: (null)]
        type: str

- login
        User to create on virtual machine, required for linux instances.
        Required together with `public_ssh_key'.
        Required with `state=present', mutually exclusive with `metadata'.
        [Default: (null)]
        type: str

- max_retries
        Max retries to proceed operation/state.
        [Default: 5]
        type: int

- memory
        RAM size, GB.
        [Default: 2]
        type: int

- metadata
        Metadata to be translate to vm.
        [Default: (null)]
        type: dict

= name
        Virtual machine name - must be unique throw all folders of cloud.

        type: str

- operation
        stop, start or get_info.
        Mutually exclusive with `state'.
        [Default: (null)]
        choises: start, stop, get_info, update

- platform_id
        Platform id.
        [Default: Intel Broadwell.]
        choises: Intel Cascade Lake, Intel Broadwell
        type: str

- preemptible
        Create preemtible(may be stopped after working 24h a row) vm.
        [Default: False]
        type: bool

- public_ssh_key
        Created user`s openssh public key.
        Required together with `public_ssh_key'.
        Required with `state=present', mutually exclusive with `metadata'.
        [Default: (null)]
        type: str

- retry_multiplayer
        Retry multiplayer between retries to proceed operation/state
        (wait retry_multiplayer*curent_retry seconds)
        [Default: 2]
        type: int

- secondary_disks_spec
        Additional disk configuration spec.
        [Default: (null)]
        type: list

- state
        VM state.
        Mutually exclusive with `operation'.
        (Choices: present, absent)[Default: (null)]
        type: str

- subnet_id
        Network id.
        Required with `state=present'
        [Default: (null)]

= token
        Oauth token to access cloud.

        type: str

- zone_id
        Availability zone id.
        [Default: ru-central1-a]
        choises: ru-central1-a, ru-central1-b, ru-central1-c
        type: str


AUTHOR: Rotaru Sergey (rsv@arenadata.io)
        METADATA:
          status:
          - preview
          supported_by: community
```
