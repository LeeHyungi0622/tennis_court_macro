from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import os

#launch url
url = "https://yeyak.seoul.go.kr/web/main.do"

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

# 초기 팝업 닫기 버튼 클릭
popup_close_button = driver.find_element("class name", "pop_x")
popup_close_button.click()

# driver.implicitly_wait(3000)

# Sports 메뉴 클릭
menu_div_element = driver.find_element("css selector", "div.ul-wrap")
menu_ul_element = menu_div_element.find_element("css selector", "ul")
menu_li_element = menu_div_element.find_elements("css selector", "li")

for li in menu_li_element:
    anchor_tag = li.find_element("tag name", "a")[1]
    print(anchor_tag.get_attribute("innerHTML"))
# sports_menu_link.click()

# sports_menu_link.click()
# print(sports_menu_link.get_attribute("innerHTML"))

# Tennis court 선택
# sort_of_sports = driver.find_elements("tag name", "a")

# for e in sort_of_sports:
#     print (e)



# Click 언어 설정 hover menu
# language_hover_menu = driver.find_elements("class name", "language")
# actions.move_to_element(language_hover_menu).perform()

# kor_language = driver.find_elements("class name", "kor")
# kor_language.click()

# 언어 한국어로 고정 
# language_setup_button = driver.find_element_by_link_text("Sports").click()
# kor_lang_button = driver.find_element("class name", "kor")
# kor_lang_button.click()