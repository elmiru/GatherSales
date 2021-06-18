from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import time

import pyperclip

def bamin_gather():

    url = 'https://ceo.baemin.com/self-service?utm_source=ceo&utm_campaign=self&utm_medium=top'
    uid = 'jukstory'
    upw = '!Ican970087!'

    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    driver.get(url)
    time.sleep(2)

    tag_id = driver.find_element_by_name('id')
    tag_id.click()
    pyperclip.copy(uid)
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    tag_pw = driver.find_element_by_name('pw')
    tag_pw.click()
    pyperclip.copy(upw)
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    #Login button click
    login_btn = driver.find_element(By.CLASS_NAME,'button')
    login_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #https://ceo.baemin.com/self-service/orders/history
    driver.get("https://ceo.baemin.com/self-service/orders/history")
    driver.implicitly_wait(10)
    time.sleep(2)

    #바로결제
    #/html/body/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/select[4]/option[2]
    xpath = "/html/body/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/select[4]/option[2]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    time.sleep(2)

    #date picker select
    xpath = "/html/body/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    time.sleep(2)

    #Select today
    today = driver.find_element(By.CLASS_NAME,'DayPicker-Day--today')
    today.click()
    time.sleep(2)

    #date picker select
    xpath = "/html/body/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    time.sleep(2)

    #조회
    xpath = "/html/body/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/button"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")
    time.sleep(2)

    if [] == soup.select('dl.DataList'):
        cash_pay = '0'
    else:
        cash_pay = soup.select('dd')[1].text
        cash_pay = cash_pay.split(' ')[0]

    time.sleep(1)

    #만나서결제
    xpath = "/html/body/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/select[4]/option[3]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #조회
    xpath = "/html/body/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/button"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")
    time.sleep(1)

    if [] == soup.select('dl.DataList'):
        meet_pay = '0'
    else:
        meet_pay = soup.select('dd')[1].text
        meet_pay = meet_pay.split(' ')[0]

    driver.close()
#    display.stop()

    time.sleep(2)

    return cash_pay, meet_pay
