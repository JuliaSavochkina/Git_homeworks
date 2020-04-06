import concurrent.futures
from redis_funcs import download_to_redis
from get_info import gen_links, auth
from private_info import client_id
import time




start_time = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    gen = gen_links(auth(client_id))
    for each in gen:
        executor.submit(download_to_redis, each).result()  # потому что подаю по ссылке, а не листом
print("--- %s seconds ---" % (time.time() - start_time))
