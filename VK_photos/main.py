import concurrent.futures
from redis_funcs import download_to_redis
from get_info import gen_links


with concurrent.futures.ThreadPoolExecutor() as executor:
    gen = gen_links()
    print(gen)
    for each in gen:
        executor.submit(download_to_redis, each).result()  # потому что подаю по ссылке, а не листом
