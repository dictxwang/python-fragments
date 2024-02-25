# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip install pyautogui==0.9.54
'''

import pyautogui
import time


if __name__ == '__main__':

    pyautogui.moveTo(400, 200)
    pyautogui.moveTo(450, 200)
    pyautogui.rightClick()
    time.sleep(3)
    pyautogui.moveTo(480, 490)
    pyautogui.click()

    time.sleep(30)
