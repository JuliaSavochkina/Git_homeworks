import xml.etree.ElementTree as ET
import requests
from functools import reduce
import datetime
import time



def loader(url_string, dataset):
    r = requests.get(url_string)
    if r.status_code == 200:
        root = ET.fromstring(r.text)
        order = {}
        for payment_list in root:
            for payment in payment_list:
                order[payment.tag] = payment.text
            dataset.append(order)
        return dataset
    else:
        print('Ваш звонок очень важен для нас, попробуйте запросить позднее...')

# url_string = 'http://printbar.advcake.com/export/admitad?pass=q8q77yzh4IGPYkiHjgGcvBGdbF3Jbh3J'
url_string = 'https://adspire.io/reports/admitad_actions/11767/mixit.ru/admitad/6raIpdDU'
dataset = []

loader(url_string, dataset)
print(dataset)


dataset = [{'uid': '83f8aa6aee6af6337c999ce0b5d9af', 'order_id': '13', 'tariff_code': '1', 'action_code': '1',
            'price': '100', 'quantity': '1', 'product_id': '1529675', 'payment_type': 'sale', 'currency_code': 'RUB',
            'position_count': '2', 'position_id': '1', 'datetime_action': '2019-07-15 22:29:09'},
           {'uid': '83f8aa6aee6af6337c999ce0b5d9af356', 'order_id': '17', 'tariff_code': '', 'action_code': '1',
            'price': '200', 'quantity': '1', 'product_id': '1529675', 'payment_type': 'sale', 'currency_code': 'RUB',
            'position_count': '2', 'position_id': '2', 'datetime_action': '2019-07-15 22:29:09'},
           {'uid': '83f8aa6aee6af6337c999ce0b5d9af36', 'order_id': '', 'tariff_code': '1', 'action_code': '1',
            'price': '400', 'quantity': '3', 'product_id': '1529675', 'payment_type': 'sale', 'currency_code': 'RUB',
            'position_count': '1', 'position_id': '1', 'datetime_action': '2019-07-15'},
           {'uid': '83f8aa6aee6af6337c999ce0b5d9af36', 'order_id': '14', 'tariff_code': '1', 'action_code': '1',
            'price': '400', 'quantity': '3', 'product_id': '1529675', 'payment_type': 'sale', 'currency_code': 'RUB',
            'position_count': '1', 'position_id': '1', 'datetime_action': '2019-07-15'},
           {'uid': '83f8aa6aee6af6337c999ce0b5d9af39', 'order_id': '25', 'tariff_code': '', 'action_code': '0',
            'price': '400', 'quantity': '3', 'product_id': '1529675', 'payment_type': 'sale', 'currency_code': 'RUB',
            'position_count': '1', 'datetime_action': '2019-07-15 22:29:09'}]

# 1)проверить что ключи присутствуют (не работает oneliner)
def key_present(dataset):
    keys = ['uid', 'order_id', 'tariff_code', 'action_code', 'price', 'quantity', 'product_id', 'payment_type',
            'currency_code', 'position_count', 'position_id', 'datetime_action']
    for each in dataset:
        if len(each.keys()) != len(keys):
            print('Недостаточно полей для сбора заказа order_id = ' + each['order_id'])
    # return = list(map(lambda keys, dataset: print('Недостаточно данных для обработки order_id=' + y['order_id'])
    #                      for x in keys for y in dataset if x != y), dataset)

# 2) проверить длину uid (вроде работает)
def length_checker(dataset):
    # length = list(filter(None, map(lambda x: x['order_id'] if len(x['uid']) != 32 else None, dataset)))
    # if len(length) != 0:
    #     print(f'Uid невалидный')
    #     print(length)
    for each in dataset:
     if len(each['uid']) != 32:
         order = each['order_id']
         print(f'Uid невалидный для order_id = {order}')


# 3) проверить что заказ - не пустая строка (работает, но дополнительно возвращает пустой лист - хз почему)
def empty_order(dataset):
    return list(filter(None, map(lambda x: print('Пустой заказ для uid = ' + x['uid']) if x['order_id'] == '' else None, dataset)))


# 4) проверить формат даты (не работает для oneliner)
def date_format(dataset):
    for each in dataset:
        try:
            time.strptime(each['datetime_action'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print('Проверьте дату для order_id = ' + each['order_id'])
    # return list(filter(None, map(lambda x: print('Проверьте дату для order_id =' + x['order_id']) if
    #         time.strptime(x['datetime_action'], '%Y-%m-%d %H:%M:%S') is ValueError else None, dataset)))


# 5) проверить что заполнен тариф код и экшн код с использованием filter (только для tariff_code)
def ac_tc(dataset):
    return list(filter(
        lambda x: print('Пустой tariff_code для order_id = ' + x['order_id']) if x['tariff_code'] == '' else 0, dataset))
    # Это работает, но это не oneliner
    # for each in dataset:
    #     if (each['tariff_code'] is '') or (each['action_code'] is ''):
    #         order = each['order_id']
    #         print(f'Не указан код дейсвтия или тарифа order_id = {order}')


# переводит поля прайс в соответствии с rate. использовать map.
# def mapper(dataset, rate, n_dataset):
#     n_dataset = dataset.copy()
#     for each in n_dataset:
#         if each.keys() == 'price':
#             float(each.value())*rate
#     print(n_dataset)


# считает нашу комиссию по всем заказам. использовать reduce. (не работает)
# def money(dataset, com_rate):
#     return reduce(lambda x, y: (x['price'])*com_rate + (y['price'])*com_rate, dataset)

def checker (dataset):
    # if key_present(dataset) is None:
    print(key_present(dataset))
    print(length_checker(dataset))
    print(empty_order(dataset))
    print(ac_tc(dataset))
    print(date_format(dataset))
    # else:
    #     print(key_present(dataset))

# with open('awesome_task.txt', 'w') as file:
#     file.write(checker(dataset))
