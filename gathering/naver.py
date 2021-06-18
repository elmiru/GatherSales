from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import time

import pyperclip

def naver_gather():

    url = 'https://nid.naver.com/nidlogin.login?svctype=1&locale=ko_KR&url=https%3A%2F%2Fpartner.booking.naver.com%2Fbizes'
    uid = 'juk-story'
    upw = '!ican12083425!'

    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    driver.get(url)
    time.sleep(1)

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

    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    xpath = "/html/body/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/a"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    time.sleep(2)

    xpath = "/html/body/div/div/div[2]/div[1]/div/div/div[1]/nav/ul/li[7]/a"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    time.sleep(2)

    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")

    매출액 = soup.select('span.StatisticsSummary__sales-number__2aJNz')[0].text

    driver.close()
#    display.stop()

    time.sleep(2)

    return 매출액
