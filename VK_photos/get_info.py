from private_info import client_id
import requests
from selenium_funcs import selen


def auth(client_id: str, scope: str = 'photos') -> str:
    auth_url = f'https://oauth.vk.com/authorize?client_id={client_id}&display=page&' \
               f'redirect_uri=https://oauth.vk.com/blank.html&scope={scope}&response_type=token&v=5.103'
    auth_token: str = selen(auth_url)
    return auth_token


def gen_links(token: str) -> list:
    try:
        url: str = 'https://api.vk.com/method/photos.getAll'
        params: dict = {'v': '5.52',
                        'access_token': token,
                        'count': '100'}

        data: dict = requests.get(url, params).json()['response']['items']

    except requests.exceptions.RequestException as error:
        print(error)

    else:
        while True:
            for i in range(len(data)):
                try:
                    yield data[i]['photo_1280']
                    i += 1
                except KeyError:
                    yield data[i]['photo_604']
                    i += 1
            else:
                break


if __name__ == '__main__':
    token = auth(client_id)
    # print(token)
    gen = gen_links(token)
    for each in gen:
        print(each)
