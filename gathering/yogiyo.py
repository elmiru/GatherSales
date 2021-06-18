from selenium import webdriver
from selenium.webdriver.common.by import By

#from pyvirtualdisplay import Display

from bs4 import BeautifulSoup
import time

def yogiyo_gather():

    url = 'https://owner.yogiyo.co.kr/owner/login/'
    uid = 'jukstory'
    upw = '!Ican970087!'

#    display = Display(visible=0, size=(1024,768))
#    display.start()

    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#    driver.set_window_size(1024, 768)

    #time.sleep(2)
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)

    #ID 입력
    tag_id = driver.find_element_by_id("username")
    tag_id.send_keys(uid)

    #Password 입력
    tag_pw = driver.find_element_by_id("password")
    tag_pw.send_keys(upw)

    #Login button click
    xpath = "//button[@class = 'button']"
    login_btn = driver.find_element_by_xpath(xpath)
    login_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #비밀번호변경요청
    xpath = "/html/body/div[4]/div[3]/a[1]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #datepicker
    #/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/div/input[1]
    xpath = "/html/body/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/div/input[1]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #/html/body/div[5]/div/a[2]
    xpath = "/html/body/div[5]/div/a[2]"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #<td class=" ui-datepicker-days-cell-over  ui-datepicker-today" data-handler="selectDay" data-event="click" data-month="4" data-year="2021"><a class="ui-state-default ui-state-highlight" href="#">25</a></td>
    #xpath = "//td[@class = ' ui-datepicker-days-cell-over  ui-datepicker-today']"
    today_picker = driver.find_element(By.CLASS_NAME, 'ui-datepicker-today')
    today_picker.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    #조회하기
    #/html/body/div[3]/div[2]/form/div[2]/button
    xpath = "/html/body/div[3]/div[2]/form/div[2]/button"
    sel_btn = driver.find_element_by_xpath(xpath)
    sel_btn.click()
    driver.implicitly_wait(10)
    time.sleep(2)

    req = driver.page_source
    soup = BeautifulSoup(req, "html.parser")

    table = soup.find('table', class_='order-summary-table')
    value = table.find_all('li')

    온라인결제 = value[2].find_all('span')[1].text
    온라인결제 = 온라인결제.replace('원','')
    만나서결제 = value[3].find_all('span')[1].text
    만나서결제 = 만나서결제.replace('원','')

    driver.close()
#    display.stop()

    time.sleep(2)

    return 온라인결제, 만나서결제
