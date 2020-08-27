from selenium import webdriver
import DriverTool
import Website
import Tool


def Baidu_search(driver, keyword):
    driver: webdriver.Chrome
    try:
        DriverTool.safe_get_element(driver=driver, path='//*[@id="kw"]', timeout=2)
    except:
        Website.to_Baidu(driver)
    DriverTool.safe_send_keys(driver=driver, path='//*[@id="kw"]', keyword=keyword, timeout=2)
    DriverTool.safe_click(driver=driver, path='//*[@id="su"]', timeout=2)
    return True


def get_Baidu_datas(driver):
    datas = []
    driver: webdriver.Chrome
    DriverTool.safe_get_element(driver=driver, path='//div[contains(@class, "c-container")]', timeout=5)
    contentx = Tool.to_xml(driver.page_source)
    container_xs = Tool.xpath_all(contentx, '//div[contains(@class, "c-container")]')
    for container_x in container_xs:
        title = Tool.xpath_union(container_x, path='./h3/a//text()')
        href = Tool.xpath_one(container_x, path='./h3/a//@href')
        id = Tool.xpath_one(container_x, path='./@id')
        try:
            id = int(id)
        except:
            id = None
        datas.append({'id': id, 'title': title, 'href': href})
    return datas
