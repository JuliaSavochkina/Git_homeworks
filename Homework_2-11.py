from selenium import webdriver
import number_week  
import requests
from selenium.webdriver.chrome.options import Options

url = 'https://dev-crm.admitad.com/company/personal/user/180/tasks/task/edit/0/?TEMPLATE=197&SUBTASK_BY_TEMPLATE=Y&PARENT_TASK_ID=153258'

# check if the site is available
if requests.get(url).status_code == 200:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=chrome_options)
    browser.implicitly_wait(5)
    browser.get(url)

    # Authorization
    browser.find_element_by_name('USER_LOGIN').send_keys('j.savochkina@admitad.com')
    browser.find_element_by_name('USER_PASSWORD').send_keys('L4KcJWn9Ef6ef5')
    browser.find_element_by_class_name('login-btn').click()

    # 2fa
    two_fa = input('Введите 2fa ключ: ')
    browser.find_element_by_name('USER_OTP').send_keys(two_fa)
    browser.find_element_by_class_name('login-btn').click()
    try:
        browser.find_element_by_class_name('errortext').text == 'Неверный одноразовый пароль.'
        two_fa2 = input('Неверный пароль. Попробуйте снова: ')
        browser.find_element_by_name('USER_OTP').send_keys(two_fa2)
        browser.find_element_by_class_name('login-btn').click()
    except:
        pass

    # task editing
    browser.find_element_by_css_selector('#task-form-bitrix_tasks_task_default_1 > div.task-info > div.task-info-panel > div.task-info-panel-title > input[type=text]').clear()
    browser.find_element_by_css_selector('#task-form-bitrix_tasks_task_default_1 > div.task-info > div.task-info-panel > div.task-info-panel-title > input[type=text]').send_keys(f'Дежурство в Sentry {number_week.week()} неделя')
    browser.find_element_by_class_name('ui-btn.ui-btn-success').click()

    # check if task created
    link = browser.current_url
    if browser.find_element_by_class_name('ui-notification-balloon-message').text == 'Задача успешно добавлена':
        print('Задача создана успешно \n'
              'Ссылка на таск ' + link)
    else:
        print('Что-то пошло не так')
else:
    print('Сайт недоступен')