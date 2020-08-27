from selenium import webdriver
import time


def get_driver() -> webdriver.Chrome:
    # selenium的options配置
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://119.114.77.174:24122')  # 代理IP
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # chrome_options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
    # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # 实例化driver
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\asus\AppData\Local\Google\Chrome\Application\chromedriver.exe',
        options=chrome_options
    )
    # 防止selenium被监测
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    return driver


def safe_get_element(driver, path, timeout=5, retry_delay=0.2):
    driver: webdriver.Chrome
    start_time = time.time()
    while True:
        try:
            return driver.find_element_by_xpath(path)
        except:
            if time.time() - start_time >= timeout:
                raise Exception('Not found %s' % str(path))
            else:
                time.sleep(retry_delay)


def safe_click(driver, path, timeout=5, retry_delay=0.2):
    # return True | raise Error
    safe_get_element(driver, path, timeout, retry_delay).click()
    return True


def safe_send_keys(driver, path, keyword, timeout=5, retry_delay=0.2):
    # return True | raise Error
    element = safe_get_element(driver, path, timeout, retry_delay)
    element.clear()
    element.send_keys(keyword)
    return True
