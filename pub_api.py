import requests
import keys
import json
import random
import csv


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
    while i < 7:
        req = json.loads(
                    get_info('https://api.admitad.com/statistics/actions/?date_start=2019-11-01&date_end=2019-12-01&limit=500&offset='+ str(i*500)))['results']
        i += 1
        data.append(req)
    return data


def orders(data):
    orders = [['order_id', 'cart', 'action_date', 'payment', 'paid', 'subid1']]
    paid = [0, 1]
    subid1 = ['Дилли', 'Вилли', 'Тилли']
    for lst in data:
        for dic in lst:
            order = []
            order.append(dic[orders[0][0]])
            order.append(dic[orders[0][1]])
            order.append(dic[orders[0][2]])
            order.append(dic[orders[0][3]])
            order.append(random.choice(paid))
            order.append(random.choice(subid1))
            orders.append(order)
    return orders


def csv_loader(orders):
    with open('orders.csv', mode='a', encoding='utf-8', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=';')
        writer.writerows(orders)


csv_loader(orders(data()))

