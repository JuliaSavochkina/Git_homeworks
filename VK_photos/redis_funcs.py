import redis
import requests


"""docker pull redis
docker run -p 6379:6379 --rm --name redis_VK redis
Чтобы подключить redis-cli, запустите еще один докер:
docker run -it --link redis:redis --rm redis redis-cli -h redis -p 6379"""


def download_to_redis(image_url: str) -> None:
    img_name = image_url.split('/')[6]
    with redis.Redis() as r:
        img = requests.get(image_url).content
        r.set(img_name, img)
        print(f"{img_name} was downloaded")


def get_value_from_redis(key: str) -> str:
    with redis.Redis() as r:
        return r.get(key)


if __name__ == '__main__':
    image_url = "https://sun9-62.userapi.com/c9883/u636052/-6/x_0f1c9741.jpg"
    download_to_redis(image_url)
    print(get_value_from_redis("x_0f1c9741.jpg"))
