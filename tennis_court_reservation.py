from selenium import webdriver
from selenium.webdriver.common.by import By
from common_func import closePopupDialog
from main_logic_function import login, mainCategorySetup, chooseAvailablePlaces
import time


url = "https://yeyak.seoul.go.kr/web/main.do"

user_id = "사용자 아이디"
user_password = "사용자 비밀번호"
reservation = "족구장"


def initialDriverSetup(url=url):
    driver = webdriver.Chrome()
    driver.set_window_size(1400,1000)
    driver.implicitly_wait(30)
    driver.get(url)
    return driver


if __name__ == '__main__':
    # 초기 driver setup
    driver = initialDriverSetup(url=url)

    # 로그인
    login(driver=driver, user_id=user_id, user_pwd=user_password)
    
    """
    접수중인 장소만 출력되도록 처리
    # 체육시설 [선택] - 종목 선택 - 상세 검색에서 "접수중" 필터 후 "상세검색"
    """
    mainCategorySetup(driver=driver, reservation=reservation)

    # 현재 접수중인 장소들을 순차적으로 예약 시도
    chooseAvailablePlaces(driver=driver)

    time.sleep(1000000)