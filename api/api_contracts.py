from typing import List

from pydantic import BaseModel, Extra


class RegletImage(BaseModel):
    name: str


class Reglet(BaseModel):
    id: int
    ip: str
    name: str
    size_slug: str
    status: str
    image: RegletImage


class APIContract(BaseModel):
    class Config:
        extra = Extra.allow


class APIContractGetBalance(APIContract):
    balance: float
    bonus_balance: float
    days_left: int
    hourly_cost: float
    hours_left: int
    monthly_cost: float
    state: str


class APIContractGetReglets(APIContract):
    reglets: List[Reglet]


# a = {
#     "links": {"actions": []},
#     "reglets": [
#         {
#             "archived_at": None,
#             "backups_enabled": 0,
#             "created_at": "2021-04-16 12:08:42",
#             "disk": 50,
#             "hostname": "80-78-246-47.cloudvps.regruhosting.ru",
#             "id": 762463,
#             "image": {
#                 "created_at": "2021-04-16 10:34:53",
#                 "distribution": "centos-7",
#                 "id": 762383,
#                 "min_disk_size": "5",
#                 "name": "BrainyCP",
#                 "private": 0,
#                 "region_slug": "msk1",
#                 "size_gigabytes": "4.4",
#                 "slug": "centos-7-amd64-brainycp",
#                 "type": "application",
#             },
#             "image_id": 762383,
#             "ip": "80.78.246.47",
#             "ipv6": "2a00:f940:2:4:2::2821",
#             "last_backup_date": None,
#             "link_token": None,
#             "locked": 0,
#             "memory": 1024,
#             "name": "Black Livermorium",
#             "ptr": "80-78-246-47.cloudvps.regruhosting.ru",
#             "region_slug": "msk1",
#             "service_id": 31403495,
#             "size": {
#                 "archived": 0,
#                 "disk": 50,
#                 "id": 1045,
#                 "memory": 1024,
#                 "name": "Cloud-2a",
#                 "price": "0.71428",
#                 "price_month": 480,
#                 "slug": "cloud-2a",
#                 "vcpus": 2,
#                 "weight": 30,
#             },
#             "size_slug": "cloud-2a",
#             "status": "active",
#             "sub_status": None,
#             "vcpus": 2,
#             "vpcs": [],
#         },
#         {
#             "archived_at": None,
#             "backups_enabled": 0,
#             "created_at": "2021-04-16 15:16:22",
#             "disk": 50,
#             "hostname": "194-67-92-207.cloudvps.regruhosting.ru",
#             "id": 762745,
#             "image": {
#                 "created_at": "2021-04-16 10:34:53",
#                 "distribution": "centos-7",
#                 "id": 762383,
#                 "min_disk_size": "5",
#                 "name": "BrainyCP",
#                 "private": 0,
#                 "region_slug": "msk1",
#                 "size_gigabytes": "4.4",
#                 "slug": "centos-7-amd64-brainycp",
#                 "type": "application",
#             },
#             "image_id": 762383,
#             "ip": "194.67.92.207",
#             "ipv6": "2a00:f940:2:4:2::28ec",
#             "last_backup_date": None,
#             "link_token": None,
#             "locked": 0,
#             "memory": 1024,
#             "name": "Amethyst Lanthanum",
#             "ptr": "194-67-92-207.cloudvps.regruhosting.ru",
#             "region_slug": "msk1",
#             "service_id": 31403495,
#             "size": {
#                 "archived": 0,
#                 "disk": 50,
#                 "id": 1045,
#                 "memory": 1024,
#                 "name": "Cloud-2a",
#                 "price": "0.71428",
#                 "price_month": 480,
#                 "slug": "cloud-2a",
#                 "vcpus": 2,
#                 "weight": 30,
#             },
#             "size_slug": "cloud-2a",
#             "status": "active",
#             "sub_status": None,
#             "vcpus": 2,
#             "vpcs": [],
#         },
#     ],
# }
