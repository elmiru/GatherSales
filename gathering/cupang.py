from selenium import webdriver

#from pyvirtualdisplay import Display

from bs4 import BeautifulSoup

import time

def cupang_gather():

    url = 'https://store.coupangeats.com/merchant/management/settlement/154036'
    uid = '4864400135'
    upw = '@coupang1'

#    display = Display(visible=0, size=(1024,768))
#    display.start()

    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#    driver.set_window_size(1024, 768)

    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)

    #ID 입력
    tag_id = driver.find_element_by_id("loginId")
    tag_id.send_keys(uid)

    #Password 입력
    tag_pw = driver.find_element_by_id("password")
    tag_pw.send_keys(upw)

    #Login button click
    #<button type="submit" class="btn merchant-submit-btn">로그인</button>
    xpath = "//button[@class = 'btn merchant-submit-btn']"
    login_btn = driver.find_element_by_xpath(xpath)
    login_btn.click()
    driver.implicitly_wait(10)
    time.sleep(10)

    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")
    time.sleep(2)

    if soup.select('div.dialog-title-wrapper') :
        #/html/body/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/span
        xpath = "/html/body/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/span"
        sel_btn = driver.find_element_by_xpath(xpath)
        sel_btn.click()
        time.sleep(1)

    #매출관리
    #/html/body/div/div/nav/div[2]/ul/li[1]/a/span[2]
    xpath = "/html/body/div/div/nav/div[2]/ul/li[1]/a/span[2]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #datepicker select
    #/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[1]
    xpath = "/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[1]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #오늘 select
    #/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[2]/div[3]/div/div[1]/div/label
    xpath = "/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[2]/div[3]/div/div[1]/div/label"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #datepicker select
    #/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[1]
    xpath = "/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[1]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #조회 select
    #/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/button
    xpath = "/html/body/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/button"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")
    time.sleep(2)

    if [] == soup.select('div.h1-txt > span'):
        cash_pay = '0'
    else:
        cash_pay = soup.select('div.h1-txt > span')[0].text

    driver.close()
#    display.stop()

    time.sleep(2)

    return cash_pay
