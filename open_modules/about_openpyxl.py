#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip install openpyxl==3.0.9
'''

from openpyxl import load_workbook


if __name__ == '__main__':

    rfile = "data/openpyxl_sample.xlsx"
    wb = load_workbook(rfile)
