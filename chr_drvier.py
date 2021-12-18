import chromedriver_autoinstaller


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from subprocess import CREATE_NO_WINDOW
import time
import pyperclip
import codecs
import json
import os


path = chromedriver_autoinstaller.install('./')



def clipboard_input(driver, user_xpath, user_input):
    temp_user_input = pyperclip.paste()

    pyperclip.copy(user_input)
    driver.find_element(By.XPATH, user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    pyperclip.copy(temp_user_input)
    time.sleep(1)




def DriverSession():
    with codecs.open('info.txt', 'r', encoding='utf-8') as f:
        load_account_info = json.loads(f.read())[0]
        naver_id = load_account_info['네이버_아이디']
        naver_pw = load_account_info['네이버_비밀번호']

    options = Options()
    options.add_experimental_option('prefs', {'download.default_directory':os.path.abspath('./tmp')})
    options.add_experimental_option("excludeSwitches" , ["enable-automation", "load-extension", "enable-logging"])

    chrome_service = ChromeService(path)
    chrome_service.creationflags = CREATE_NO_WINDOW
    driver = Chrome(options=options, service=chrome_service)
    driver.maximize_window()

    driver.get('https://ai.webtoons.com/painter/paint')

    driver.find_element(By.XPATH, '//img[@alt="naver"]').click()
    time.sleep(1)

    clipboard_input(driver, '//*[@id="id"]', naver_id)
    clipboard_input(driver, '//*[@id="pw"]', naver_pw)
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
    time.sleep(1)

    return driver


# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# k = [
#     r'C:\Users\power\Desktop\Project\Dev\EhndWebTranslate\filetest\bg3.JPG',
#     r'C:\Users\power\Desktop\Project\Dev\EhndWebTranslate\filetest\01.jpg',
#     r'C:\Users\power\Desktop\Project\Dev\EhndWebTranslate\filetest\bg2.JPG'
# ]


# driver = DriverSession()

# for i in range(3):

#     f = k[i]#r'C:\Users\power\Desktop\Project\Dev\EhndWebTranslate\filetest\bg3.JPG'

#     driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(f)

#     time.sleep(1)

#     driver.find_element(By.XPATH, '//button[text()="채색하기"]').click()

#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[text()="기본 모델"]')))
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)


#     driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[3]/div[2]/label').click()
#     driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[3]/div[2]/label').click()
#     time.sleep(1)

#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[5]/button'))).click()
#     driver.find_element(By.XPATH, '//*[text()="PNG로 저장하기"]').click()
#     time.sleep(2)
#     driver.get('https://ai.webtoons.com/painter/paint')
#     Alert(driver).accept()

# driver.close()