from bs4 import BeautifulSoup
import requests

url = 'https://litnet.com/ru/reader/temnyi-vlastelin-zhelaet-razvlechsya-b158309'
book = requests.get(url).text

with open('book.txt', mode='w', encoding='utf-8') as txt_file:
    soup = BeautifulSoup(book, 'html.parser')
    txt_file.write(str(soup.find('a', href='/ru/book/temnyi-vlastelin-zhelaet-razvlechsya-b158309').text) + '\n')
    txt_file.write(str(soup.h2.text) + '\n')
    paragraphs = soup.find_all('p', attrs={'style': 'text-align:justify'})
    for par in paragraphs:
        txt_file.write(str(par.text) + '\n')
