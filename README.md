# ansible-module-yandex-cloud

## Overview

*ansible-module-yandex-cloud* is a set of ansible modules that manage Yandex Cloud resources.

Examples are available as [separete repository](https://github.com/emelianov/ansible-module-yandex-cloud-cookbook).

## Build & Run

#### Prerequisites

* The <https://github.com/yandex-cloud/python-sdk> module is required.

#### Installation

1. pip install --user `git+https://github.com/yandex-cloud/python-sdk`
2. git clone `https://github.com/emelianov/ansible-module-yandex-cloud`
3. cd ansible-module-yandex-cloud

## Documentation

### ycc_vm

| Parameters | Comment |
| ---------- | ------- |
| assign_public_ip<br>*bool* | Assign public address<br>**False** - Default |
| core_fraction<br>*int*<br>5,20,50,100 | Guaranteed vCPU share<br>**100** - Default |
| cores<br>*int* | vCPU number<br>**2** - Default |
| disk_size<br>*int* | Primary disk size in GB<br>**10** - Default |
| disk_type<br>*str*<br>hdd,sdd | Primary disk type<br>**hdd** - Default |
| folder_id<br>*str* | Virtual machine target folder id |
| hostname<br>*str* | Virtual machine hostname, default same as name<br>**null** - Default |
| image_id<br>*str* | Boot image id<br>Required with `state`=present<br>**null** - Default |
| login<br>*str* | User to create on virtual machine, required for linux instances<br>Required together with `public_ssh_key`<br>Required with `state`=present<br>**null** - Default |
| max_retries<br>*int* | Max retries to proceed operation/state<br>**5** - Default |
| memory<br>*int* | RAM size, GB<br>**2** - Default |
| metadata<br>*dict* | Metadata to be translate to vm<br>**null** - Default |
| name<br>*str* | Virtual machine name - must be unique throw all folders of cloud.
| operation<br>start,stop,get_info,update | Virtual machine control<br>Mutually exclusive with `state`<br>**null** - Default |
| platform_id<br>*str*<br>Intel Cascade Lake, Intel Broadwell | Platform id<br>Intel Broadwell - Default]
| preemptible<br>*bool* | Create preemtible(may be stopped after working 24h a row) vm<br>**false** - Default |
| public_ssh_key<br>*str* | Created user's openssh public key<br>Required together with `login`<br>Required with `state`=present, mutually exclusive with `metadata`<br>**null** - Default |
| retry_multiplayer<br>*int* | Retry multiplayer between retries to proceed operation/state (wait retry_multiplayer*curent_retry seconds)<br>**2** - Default |
| secondary_disks_spec<br>*list* | Additional disk configuration spec<br>**null** - default |
| state<br>*str*<br>present,absent | VM state<br>Mutually exclusive with `operation`<br>**null** - Default
| subnet_id<br>*str* | Network id<br>Required with `state`=present<br>**null** - Default |
| auth/token<br>*str* | Oauth token to access cloud. |
| zone_id<br>*str*<br>ru-central1-a, ru-central1-b, ru-central1-c | Availability zone id<br>**ru-central1-a** - Default

Maintainer: Alexander Emelianov (a.m.emelianov@gmail.com)

Author of original library: Rotaru Sergey (rsv@arenadata.io)
