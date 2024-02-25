# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import pyautogui

'''
通过selenium模拟用户操作浏览器，需要下载对应浏览器的driver，如：
chromedriver for chrome
geckodriver for firefox
注意driver的版本需要和浏览器版本保持一致

安装依赖
pip install selenium==4.18.1
pip install pyautogui==0.9.54
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
    }

    chrome_options.add_experimental_option('prefs', prefs)

    # 设置用户数据空间，程序执行过程会在指定路径下创建Default文件夹
    chrome_options.add_argument(r"--user-data-dir=/Users/wangqiang/Library/Application Support/Google/Chrome/Temp_Selenium_001/")

    # 设置代理
    if proxy is not None:
        chrome_options.add_argument("--proxy-server=" + proxy_type + "://" + proxy)
    elif pac is not None:
        chrome_options.add_argument("--proxy-pac-url=" + pac)

    # 加载chrome扩展程序，其中crx文件可以通过诸如CRX-Extractor-Download插件获取
    if add_extension:
        # chrome_options.add_extension(r"extension/Momentum.crx")
        chrome_options.add_extension("extension/Wizz-Wallet-Formerly-Atom.crx")
    else:
        chrome_options.add_argument("disable-extensions")

    # chrome_options.add_argument("start-maximized")  # 启动时窗口最大化

    # chrome版本和chromedriver版本需要保持一致，否则会如下错误：
    # unknown error: DevToolsActivePort file doesn't exist
    service = Service(executable_path=driver_file)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def use_extension(driver):

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60.0)
    driver.set_script_timeout(60)

    driver.get("https://starkgate.starknet.io/")
    # driver.get("https://google.com/")

    driver.maximize_window()
    time.sleep(1)

    # 获取主窗口
    main_handle = driver.window_handles[0]

    for i in range(0, len(driver.window_handles)):
        if i > 0:
            driver.switch_to.window(driver.window_handles[i])
            driver.close()
    time.sleep(1)

    # 点击插件图标，打开插件
    pyautogui.moveTo(1300, 80)
    pyautogui.click()
    time.sleep(3)

    # 切换到插件窗口
    extension_handle = None
    while True:
        for handle in driver.window_handles:
            if handle == main_handle:
                continue
            driver.switch_to.window(handle)
            divs = driver.find_elements(by=By.TAG_NAME, value="div")
            for div in divs:
                if div.text == "Make bitcoin magical again" or div.text == "Enter your password":
                    extension_handle = handle
                    break
            if extension_handle is not None:
                break
        if extension_handle is not None:
            break

    driver.switch_to.window(extension_handle)
    time.sleep(1)

    # 循环多页面交互
    finish_step_3 = False
    while True:
        divs = driver.find_elements(by=By.TAG_NAME, value="div")
        step_password = False
        step_begin_bind = False
        step_bind_1 = False
        step_bind_2 = False
        step_bind_3 = False
        step_bind_3_2 = False

        for div in divs:
            if div.text == "Enter your password":
                step_password = True
                break
            if div.text == "Make bitcoin magical again":
                step_begin_bind = True
                break
            if div.text == "Choose a wallet you want to restore from":
                step_bind_1 = True
                break
            if div.text == "Secret Recovery Phrase":
                step_bind_2 = True
                break
            if div.text == "Address Type" and not finish_step_3:
                step_bind_3 = True
                break
            if div.text == "Please be aware that:":
                step_bind_3_2 = True
                break

        if not step_password and not step_begin_bind and not step_bind_1 and not step_bind_2 and not step_bind_3 and not step_bind_3_2:
            break

        if step_password:
            # 输入口令
            inputs = driver.find_elements(by=By.TAG_NAME, value="input")
            inputs[0].send_keys("12345678")
            click_div_by_text(driver, "Unlock")

        if step_begin_bind:
            click_div_by_text(driver, "I already have a wallet")
            inputs = driver.find_elements(by=By.TAG_NAME, value="input")
            if inputs and len(inputs) == 2:
                inputs[0].send_keys("12345678")
                inputs[1].send_keys("12345678")
                time.sleep(2)
                button = driver.find_element(by=By.TAG_NAME, value="button")
                button.click()

        if step_bind_1:
            click_div_by_text(driver, "Atomicals")

        if step_bind_2:
            inputs = driver.find_elements(by=By.TAG_NAME, value="input")
            words = ["xx"] * 12
            words.reverse()
            for input in inputs:
                if input.get_attribute("type") == "password":
                    input.send_keys(words.pop())
            click_div_by_text(driver, "Continue")

        if step_bind_3:
            click_div_by_text(driver, "Continue")
            finish_step_3 = True

        if step_bind_3_2:
            # 这个插件页面的checkout不可点击，直接点击外层的div
            divs = driver.find_elements(by=By.CLASS_NAME, value="adm-checkbox-icon")
            for div in divs:
                div.click()
            time.sleep(1)
            click_div_by_text(driver, "OK")

        time.sleep(2)

    # 再次点击插件图标，关闭插件
    pyautogui.moveTo(10, 10)
    pyautogui.moveTo(1300, 80)
    pyautogui.click()

    time.sleep(1100)
    try:
        driver.close()
        driver.quit()
    except Exception as exp:
        print("Driver Close Failed")


def click_div_by_text(driver, div_text):
    divs = driver.find_elements(by=By.TAG_NAME, value="div")
    divs.reverse()
    for div in divs:
        if div.text == div_text:
            div.click()
            break


if __name__ == '__main__':

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    driver = create_driver_chrome(user_agent, headless=False, add_extension=True, os_type="mac")
    use_extension(driver)
