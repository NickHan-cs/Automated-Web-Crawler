import Service
import DriverTool
import Tool


@Tool.thread_wrapper
def spider(keyword):
    driver = DriverTool.get_driver()
    Service.Baidu_search(driver, keyword=keyword)
    datas = Service.get_Baidu_datas(driver)
    for data in datas:
        print(data)


if __name__ == '__main__':
    keywords = ['python', 'java', 'go', 'php', 'c++']
    for keyword in keywords:
        spider(keyword)
