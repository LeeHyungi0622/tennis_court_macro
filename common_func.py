from selenium import webdriver
from selenium.webdriver.common.by import By

def closePopupDialog(driver):
    # 팝업 닫기 버튼 클릭
    popup_close_button = driver.find_element(By.CLASS_NAME, "pop_x")
    popup_close_button.click()
