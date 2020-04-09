from redis_funcs import download_to_redis
from get_info import gen_links, auth
from private_info import client_id
import threading


gen = gen_links(auth(client_id))
threads = []
for each in gen:
    t1 = threading.Thread(target=download_to_redis(each))
    t1.start()
    threads.append(t1)
for thread in threads:
    thread.join()
