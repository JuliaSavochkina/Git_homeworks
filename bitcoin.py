import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def numbers(num):
    return round(float((num.replace('.', '')).replace(',', '.')), 2)


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
    user_agent = {'User-agent': 'Mozilla/5.0'}
    logs = requests.get(url, headers=user_agent).text
    soup = BeautifulSoup(logs, 'html.parser')
    a = numbers(c_price())
    first = a
    end = 0
    while -5 < end < 5:
        try:
            logs = requests.get(url, headers=user_agent).text
            soup = BeautifulSoup(logs, 'html.parser')
            date_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
            b = numbers(c_price())
            dif = round((a - b), 2)
            abs_dif = abs(dif)
            a = b
            if dif > 0:
                log.write(f'{date_time} Курс увеличился на ${abs_dif}.\n')
            elif dif < 0:
                log.write(f'{date_time} Курс уменьшился на ${abs_dif}.\n')
            else:
                continue
            time.sleep(5)
            end = first - b
        except end > 5 or end < -5:
            break
    if end > 5:
        log.write('пора продавать')
    else:
        log.write('пора покупать')
