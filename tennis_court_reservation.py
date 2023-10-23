from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

#launch url
url = "https://yeyak.seoul.go.kr/web/main.do"

user_id = "사용자 아이디"
user_password = "사용자 패스워드"
reservation = "족구장"

driver = webdriver.Chrome()
driver.set_window_size(1400,1000)
driver.implicitly_wait(30)
driver.get(url)

# 초기 팝업 닫기 버튼 클릭
popup_close_button = driver.find_element(By.CLASS_NAME, "pop_x")
popup_close_button.click()

# 로그인
state_div_el = driver.find_element(By.CLASS_NAME, "state")
login_btn_el = state_div_el.find_element(By.TAG_NAME, "a")
login_btn_el.click()

# 아이디 및 패스워드 입력
id_input_el = driver.find_element(By.ID, "userid")
id_input_el.send_keys(user_id)
pwd_input_el = driver.find_element(By.ID, "userpwd")
pwd_input_el.send_keys(user_password)

# 로그인 버튼 클릭
login_btn_el = driver.find_element(By.CLASS_NAME, "btn_login")
login_btn_el.click()

time.sleep(2)

# 로그인 후 팝업 창 닫기
popup_close_button = driver.find_element(By.CLASS_NAME, "pop_x")
popup_close_button.click()

# Sports 메뉴 클릭
sports_menu_link = driver.find_element(By.LINK_TEXT, '체육시설')
sports_menu_link.click()

# Tennis court 메뉴 클릭
tennis_category_menu = driver.find_element(By.LINK_TEXT, reservation)
tennis_category_menu.click()

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

# 현재 접수중인 장소들을 순차적으로 돌면서 예약 시도 
# 순차적으로 Thumbnail 부분 클릭 
place_list = driver.find_element(By.CLASS_NAME, "img_board")
places = place_list.find_elements(By.TAG_NAME, "li")

for place in places:
    img_div_el = place.find_element(By.CLASS_NAME, "img_box")
    # 현재 접수중인 항목의 이미지 클릭
    img_div_el.click()
    # 팝업창 내리기
    popup_close_button = driver.find_element(By.CLASS_NAME, "pop_x")
    popup_close_button.click()
    break

time.sleep(1000000)