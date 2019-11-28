import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests

# перевод из строки в число с округлением до двух знаков после запятой
def numbers(num):
    return round(float((num.replace('.', '')).replace(',', '.')), 2)

# возвращаетзначение стоимости биткоина с сайта
def c_price():
    try:
        return soup.find('td', class_='pid-1057391-last greenBg').text
    except AttributeError:
        try:
            return soup.find('td', class_='pid-1057391-last').text
        except AttributeError:
            return soup.find('td', class_='pid-1057391-last redBg').text


with open('logs.txt', mode='a', encoding='utf-8') as log:
    url = 'https://m.ru.investing.com/crypto/'
    user_agent = {'User-agent': 'Mozilla/5.0'} # сайт банил меня
    logs = requests.get(url, headers=user_agent).text
    soup = BeautifulSoup(logs, 'html.parser')
    a = numbers(c_price()) # фиксируем начало отсчета
    first = a # запоминаем его, чтобы сравнивать с текущим значением
    end = 0
    while -5 < end < 5:
        try:
            logs = requests.get(url, headers=user_agent).text
            soup = BeautifulSoup(logs, 'html.parser')
            date_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") # возвращает текущую дату/время в заданном формате
            b = numbers(c_price()) # текущее значение ячейки
            dif = round((a - b), 2) # находим изменение стоимости на текущем щаге
            abs_dif = abs(dif) # модуль изменения
            a = b # перезаписываем предыдущее значение
            if dif > 0: # если разность получилась положительной, то прирост --> курс увеличивается (записываем в файл)
                log.write(f'{date_time} Курс увеличился на ${abs_dif}.\n')
            elif dif < 0: # если разность получилась отрицательной, то убыль --> курс уменьшается (записываем в файл)
                log.write(f'{date_time} Курс уменьшился на ${abs_dif}.\n')
            else: # если изменения не было, то перейти к новому циклу
                continue
            time.sleep(5) # ожидаение 5 сек (вот тут я думаю, можно было перенести в район if)
            end = first - b # проверяем разницу между первым и текущим зачениями
        except end > 5 or end < -5: # если курс упал или вырос на 5 баксов, остановись
            break
    if end > 5:
        log.write('пора продавать')
    else:
        log.write('пора покупать')
