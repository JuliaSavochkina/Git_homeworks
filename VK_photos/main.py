import concurrent.futures
from redis_funcs import download_to_redis
from get_info import gen_links, auth
from private_info import client_id


with concurrent.futures.ThreadPoolExecutor() as executor:
    gen = gen_links(auth(client_id))
    for each in gen:
        executor.submit(download_to_redis, each)
