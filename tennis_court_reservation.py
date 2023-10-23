from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

#launch url
url = "https://yeyak.seoul.go.kr/web/main.do"

driver = webdriver.Chrome()
driver.set_window_size(1400,1000)
driver.implicitly_wait(30)
driver.get(url)

# 초기 팝업 닫기 버튼 클릭
popup_close_button = driver.find_element(By.CLASS_NAME, "pop_x")
popup_close_button.click()

# Sports 메뉴 클릭
sports_menu_link = driver.find_element(By.LINK_TEXT, '체육시설')
sports_menu_link.click()

# Tennis court 메뉴 클릭
tennis_category_menu = driver.find_element(By.LINK_TEXT, '족구장')
tennis_category_menu.click()

# 검색어 입력란에 "실내" 검색어 입력 (테스트를 위해 우선 주석처리)
# search_input_el = driver.find_element(By.NAME, 'sch_text')
# search_input_el.send_keys("실내")

# 검색버튼 클릭 (테스트를 위해 우선 주석처리)
# search_btn_el = driver.find_element(By.CLASS_NAME, "btn_ok")
# search_btn_el.click()

# 상세검색 버튼 클릭
specific_search = driver.find_element(By.XPATH, "//button[@class='btn_ok btn_plus']")

specific_search.click()

# 접수중 접수 상태 체크박스 클릭
registration_status = driver.find_element(By.CLASS_NAME, "sch_svc_sttus_R403")
registration_status.click()

# 상세검색 버튼 클릭
specific_searchBtn = driver.find_element(By.XPATH, "//button[@id='dl_focus']")
specific_searchBtn.click()

#접수중인 장소만 출력되도록 처리 (완료)





# for option in status_options:
#     print(option.get_attribute("innerHTML"))

# 상세검색 버튼 클릭

# for el in span_elms:
#     if el.find_element(By.CLASS_NAME, "status2"):
#         print(el)
# status_banners = driver.find_element(By.CLASS_NAME, "bd_label status2")

# for banner in status_banners:
#     print(banner)

time.sleep(1000000)

# driver.implicitly_wait(3000)

# Sports 메뉴 클릭
# menu_div_element = driver.find_element("css selector", "div.ul-wrap")
# menu_ul_element = menu_div_element.find_element("css selector", "ul")
# menu_li_element = menu_div_element.find_elements("css selector", "li")

# for li in menu_li_element:
#     anchor_tag = li.find_element("tag name", "a")
#     anchor_tag.click()
#     driver.implicitly_wait(30)

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