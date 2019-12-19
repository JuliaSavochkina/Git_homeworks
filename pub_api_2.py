"""Через ввод с командной строки вводишь subid и тебе выводит статистику по этому subid
в следующем формате:
Всего заказов: xxx (+)
Самый крупный заказ: на сумму xxx рублей по офферу xxx (+)
Среднее количество заказов в день: xxx
Общая сумма выплаченной комиссии по subid: общая сумма комиссии. (+)
Количество заказов, по которым ожидается выплата: Количество (+)
"""
import pub_api_1


def file(raw, subid):
    file = []
    for lst in raw:
        if lst[5] == subid:
            file.append(lst)
    return file


def max_order(file):
    prices = []
    for i in range(len(file)):
        if file[i][1] is not None:
            prices.append(file[i][1])
        else:
            prices.append(0.0)
    zakaz = 0
    for order in file:
        if order[1] == max(prices):
            zakaz = order[6]
    return [max(prices), zakaz]


def commission_approved(file):
    s = 0
    for order in file:
        if order[7] == 'approved' and order[4] == 1:
            s += order[3]
    return s


def amount_payout(file):
    i = 0
    for order in file:
        if order[4] == 1:
            i += 1
    return i


subid = input('Введите subid (Тилли/Вилли/Дилли): ')
if subid not in ['Тилли', 'Вилли', 'Дилли']:
    print('Не балуйся! Запусти программу снова.')
else:
    raw = pub_api_1.orders(pub_api_1.data())
    file = file(raw, subid)
    print(f'Всего заказов: {len(file)}')
    print(f'Самый крупный заказ: на сумму {max_order(file)[0]} рублей по офферу {max_order(file)[1]}')
    print(f'Среднее количество заказов в день: {len(file)/30}')
    print(f'Общая сумма выплаченной комиссии по subid: {commission_approved(file)}')
    print(f'Количество заказов, по которым ожидается выплата: {amount_payout(file)}')
