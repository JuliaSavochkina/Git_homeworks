import requests
import keys
import json
import random


def get_token():
    url = 'https://api.admitad.com/token/'
    payload = {
        "client_id": keys.client_id,
        "scope": 'statistics',
        "grant_type": 'client_credentials'
    }

    headers = {
        'Authorization': keys.b64
    }
    r = requests.post(url, params=payload, headers=headers)
    dict_r = r.json()
    return dict_r['access_token']


def get_info(link):
    token = get_token()
    token2 = 'Bearer ' + token
    headers2 = {
        'Authorization': token2
    }
    r2 = requests.get(link, headers=headers2)
    return r2.text

def data():
    data = []
    i = 1
    req = json.loads(
                 get_info('https://api.admitad.com/statistics/actions/?date_start=2019-11-01&date_end=2019-12-01&limit=500'))['results']
    data.append(req)
    return data


def orders(data):
    all_orders = []
    orders = ['order_id', 'cart', 'action_date', 'payment', 'paid', 'subid1', 'advcampaign_name', 'status']
    paid = [0, 1]
    subid1 = ['Дилли', 'Вилли', 'Тилли']
    status = ['pending', 'approved', 'declined']
    for lst in data:
        for dic in lst:
            order = []
            order.append(dic[orders[0]])
            order.append(dic[orders[1]])
            order.append(dic[orders[2]])
            order.append(dic[orders[3]])
            order.append(random.choice(paid))
            order.append(random.choice(subid1))
            order.append(dic[orders[6]])
            order.append(random.choice(status))
            all_orders.append(order)
    return all_orders
