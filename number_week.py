from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=chrome_options)

def week():
    browser.get('https://kalendar-365.ru/week')
    number = browser.find_element_by_class_name('current-week-number__number')
    return number.text
