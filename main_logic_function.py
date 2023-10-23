from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from common_func import closePopupDialog

def login(**kwargs):
    driver = kwargs['driver']
    user_id = kwargs['user_id']
    user_pwd = kwargs['user_pwd']

    # 초기 팝업창 닫기
    closePopupDialog(driver)

    # 로그인
    state_div_el = driver.find_element(By.CLASS_NAME, "state")
    login_btn_el = state_div_el.find_element(By.TAG_NAME, "a")
    login_btn_el.click()

    # 아이디 및 패스워드 입력
    id_input_el = driver.find_element(By.ID, "userid")
    id_input_el.send_keys(user_id)
    pwd_input_el = driver.find_element(By.ID, "userpwd")
    pwd_input_el.send_keys(user_pwd)

    # 로그인 버튼 클릭
    login_btn_el = driver.find_element(By.CLASS_NAME, "btn_login")
    login_btn_el.click()

    time.sleep(2)

    # 팝업창 닫기
    closePopupDialog(driver)


def mainCategorySetup(**kwargs):
    driver = kwargs['driver']
    reservation = kwargs['reservation']
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


def chooseAvailablePlaces(**kwargs):
    driver = kwargs['driver']
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

def chooseReservationDateAndReserve(**kwargs):
    driver = kwargs['driver']
    date = kwargs['date']
    date_td_el = driver.find_element(By.ID, f"calendar_{date}")
    date_td_el.click()
    #  예약버튼 클릭
    reservation_button = driver.find_element(By.CLASS_NAME, "common_btn")
    reservation_button.click()