from selenium import webdriver


def to_Baidu(driver):
    driver: webdriver.Chrome
    driver.get("https://www.baidu.com")
