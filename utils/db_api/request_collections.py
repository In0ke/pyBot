from enum import Enum
import time
import requests
from pydantic import BaseModel

token = '62e5dfd3cb06cb152479df9d715b88a2d3ae3e114ccf7b0d08b18fe3cb007347ab8abd5901dc645eb1d4a8f4c810c8e2'


class AuthToken(str):
    token = {'Authorization': f'Bearer {token}'}


class SizeType(str, Enum):
    cloud_1 = "cloud-1"


class Operations(str, Enum):
    reboot = 'reboot'
    stop = 'stop'
    start = 'start'


class ImageType(str, Enum):
    ubuntu20 = "ubuntu-20-04-amd64-lamp"


class PlayLoadDTO(BaseModel):
    size: SizeType
    image: ImageType


class PlayLoadOperations(BaseModel):
    type: Operations


def get_json(route=''):
    url = 'https://api.cloudvps.reg.ru/v1/'
    current_url = url + route
    request = requests.get(current_url, headers=AuthToken.token)
    response = request.json()
    return response


def create_server():
    url = 'https://api.cloudvps.reg.ru/v1/reglets'
    payload = PlayLoadDTO(size=SizeType.cloud_1, image=ImageType.ubuntu20)
    request = requests.post(url, headers=AuthToken.token, json=payload.dict())
    response = request.json()
    id = response['links']['actions'][0]['id']
    url = 'https://api.cloudvps.reg.ru/v1/actions/' + str(id)
    request = requests.get(url, headers=AuthToken.token)
    response = request.json()
    status = response['action']['status']
    while status in ['new', 'in-progress']:
        request = requests.get(url, headers=AuthToken.token)
        response = request.json()
        status = response['action']['status']
        print(status)
        time.sleep(2)
    print(status)
    return status


def get_tarif_list():
    data = get_json('sizes')
    tarif_list = []
    for number in range(0, len(data['sizes'])):
        tarif_list.append(data['sizes'][number]['name'])
        tarif_list.append('disk: ' + str(data['sizes'][number]['disk']))
        tarif_list.append('memory: ' + str(data['sizes'][number]['memory']))
        tarif_list.append('CPU: ' + str(data['sizes'][number]['vcpus']))
        tarif_list.append('price month: ' + str(data['sizes'][number]['price_month']))

    return list(zip(*[iter(tarif_list)] * 5))


def get_balance_data(args):
    data = get_json('balance_data')
    print(data['balance_data'][args])


def get_os_images():
    data = get_json('images?type=distribution')
    os_list = []
    for i in range(0, len(data['images'])):
        os_list.append(data['images'][i]['slug'])
    return os_list


def get_apps_images():
    data = get_json('images?type=application')
    apps_list = []
    for i in range(0, len(data['images'])):
        apps_list.append(data['images'][i]['name'])
    return apps_list


def get_reglet_list_1(route=''):
    url = 'https://api.cloudvps.reg.ru/v1/'
    current_url = url + route
    request = requests.get(current_url, headers=AuthToken.token)
    response = request.json()
    return [
        (value["name"], value["id"], value["ip"], value["image"]["name"])
        for value in response["reglets"]]


def get_reglet_list():
    data = get_json('reglets')
    reglet_list = []
    for i in range(0, len(data['reglets'])):
        reglet_list.append(data['reglets'][i]['name'])
        reglet_list.append(data['reglets'][i]['id'])
        reglet_list.append(data['reglets'][i]['ip'])
        reglet_list.append(data['reglets'][i]['image']['name'])

    return list(zip(*[iter(reglet_list)] * 4))


def reboot_server(server_id):
    url = f'https://api.cloudvps.reg.ru/v1/reglets/{server_id}/actions'
    payload = PlayLoadOperations(type=Operations.reboot)
    request = requests.post(url, headers=AuthToken.token, json=payload.dict())
    response = request.json()
    id = response['action']['id']
    url = 'https://api.cloudvps.reg.ru/v1/actions/' + str(id)
    request = requests.get(url, headers=AuthToken.token)
    response = request.json()
    status = response['action']['status']
    while status in ['new', 'in-progress']:
        request = requests.get(url, headers=AuthToken.token)
        response = request.json()
        status = response['action']['status']
        print(status)
        time.sleep(2)
    print(status)
    return status


def stop_server(server_id):
    url = f'https://api.cloudvps.reg.ru/v1/reglets/{server_id}/actions'
    payload = PlayLoadOperations(type=Operations.stop)
    request = requests.post(url, headers=AuthToken.token, json=payload.dict())
    response = request.json()
    id = response['action']['id']
    url = 'https://api.cloudvps.reg.ru/v1/actions/' + str(id)
    request = requests.get(url, headers=AuthToken.token)
    response = request.json()
    status = response['action']['status']
    while status in ['new', 'in-progress']:
        request = requests.get(url, headers=AuthToken.token)
        response = request.json()
        status = response['action']['status']
        print(status)
        time.sleep(2)
    print(status)
    return status
