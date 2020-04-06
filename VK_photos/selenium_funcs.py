from selenium import webdriver
import re
from private_info import client_id
from selenium.webdriver.chrome.options import Options
import requests


def selen(auth_url: str) -> str:
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    try:
        browser = webdriver.Chrome(executable_path=r'/snap/bin/chromium.chromedriver', options=chrome_options)
        browser.implicitly_wait(5)
        browser.get(auth_url)

        # Authorization
        browser.find_element_by_name('email').send_keys('Julie-Webster@ya.ru')
        browser.find_element_by_name('pass').send_keys('L4KcJWn9Ef6ef5L4KcJWn9')
        browser.find_element_by_css_selector('#install_allow').click()

        # 2fa
        if browser.find_element_by_class_name('button'):
            two_fa = input('Введите 2fa ключ: ')
            browser.find_element_by_name('code').send_keys(two_fa)
            browser.find_element_by_class_name('button').click()
            browser.implicitly_wait(3)
        # get token
        browser.get(browser.current_url)
        token_url: str = browser.current_url
        token: str = re.split(r'access_token=', re.split(r'&', token_url)[-3])[-1]
        return token

    except requests.exceptions.RequestException as error:
        print(error)


if __name__ == "__main__":
    auth_url = f'https://oauth.vk.com/authorize?client_id={client_id}&display=page&' \
               f'redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.103'
    print(selen(auth_url))
