# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
通过selenium模拟用户操作浏览器，需要下载对应浏览器的driver，如：
chromedriver for chrome
geckodriver for firefox
注意driver的版本需要和浏览器版本保持一致

安装依赖
pip install selenium==4.18.1
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def create_driver_chrome(user_agent, proxy=None, pac=None, os_type="mac", headless=False, add_extension=False, proxy_type="http"):

    if os_type == "mac":
        driver_file = "driver/chromedriver_mac64"
    elif os_type == "linux":
        driver_file = "driver/chromedriver_linux64"
    else:
        driver_file = "driver/chromedriver.exe"
    chrome_options = Options()

    if headless:
        # 采用无界面的模式
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--user-agent=" + user_agent)
    chrome_options.add_argument("--disable_gpu")
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    prefs = {
        "profile.managed_default_content_settings.images": 1,
        # "profile.managed_default_content_settings.images": 2,  # 2是阻止图片加载
        # "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        # "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    }

    chrome_options.add_experimental_option('prefs', prefs)

    # 模拟移动设备
    # mobile_emulation = {"deviceName": "iPhone 6/7/8 Plus"}
    # chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)

    # 设置用户数据空间，程序执行过程会在指定路径下创建Default文件夹
    chrome_options.add_argument(r"--user-data-dir=/Users/wangqiang/Library/Application Support/Google/Chrome/123/")

    # 设置代理
    if proxy is not None:
        chrome_options.add_argument("--proxy-server=" + proxy_type + "://" + proxy)
    elif pac is not None:
        chrome_options.add_argument("--proxy-pac-url=" + pac)

    # 加载chrome扩展程序，其中crx文件可以通过诸如CRX-Extractor-Download插件获取
    if add_extension:
        chrome_options.add_extension(r"extension/Momentum.crx")
        chrome_options.add_extension("extension/Wizz-Wallet-Formerly-Atom.crx")
    else:
        chrome_options.add_argument("disable-extensions")

    # chrome_options.add_argument("start-maximized")  # 启动时窗口最大化

    # chrome版本和chromedriver版本需要保持一致，否则会如下错误：
    # unknown error: DevToolsActivePort file doesn't exist
    service = Service(executable_path=driver_file)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def common_sample(driver):

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60.0)
    driver.set_script_timeout(60)

    driver.get("https://baidu.com/")

    # 需要截图的大小为 960 * 540（缩放时，需要考虑边框宽度）
    driver.set_window_size(1500, 800)
    time.sleep(2)

    bottom_layer = driver.find_element(value="bottom_layer")

    if bottom_layer:
        # 获取元素坐标
        left = bottom_layer.location["x"]
        top = bottom_layer.location["y"]

        # 获取元素宽高
        width = bottom_layer.size["width"]
        height = bottom_layer.size["height"]

        print(f"left={left}, top={top} / width={width}, height={height}")

    # 截图保存
    screenshot_fp = f"data/selenium_screenshot_{width}_{height}.png"
    driver.save_screenshot(screenshot_fp)

    # 获取主窗口
    main_handle = driver.window_handles[0]

    # 执行js脚本：在新窗口打开页面
    driver.execute_script("window.open('https://image.baidu.com', '_blank')")

    # 探测并切换到新窗口
    new_handle = None
    while not new_handle:
        for handle in driver.window_handles:
            if handle != main_handle:
                new_handle = handle
    driver.switch_to.window(new_handle)
    time.sleep(5)

    # 重新切回主窗口
    driver.switch_to.window(main_handle)

    time.sleep(5)
    try:
        driver.close()
        driver.quit()
    except Exception as exp:
        print("Driver Close Failed")


def type_click_sample(driver):

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60.0)
    driver.set_script_timeout(60)

    driver.get("https://baidu.com/")

    time.sleep(3)
    input = driver.find_element(value="kw")
    input.send_keys("刘德华")
    time.sleep(5)

    submit = driver.find_element(value="su")
    submit.click()

    time.sleep(5)
    try:
        driver.close()
        driver.quit()
    except Exception as exp:
        print("Driver Close Failed")


if __name__ == '__main__':

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    driver = create_driver_chrome(user_agent, headless=False, os_type="mac")
    # common_sample(driver)
    type_click_sample(driver)
