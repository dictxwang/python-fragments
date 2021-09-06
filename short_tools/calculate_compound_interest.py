# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import math


def circle_rate(rate=1, times=1):
    '''
    计算一个周期内本息百分数
    :param rate: 利率
    :param times: 计息次数
    :return:
    '''
    return math.pow((1 + (rate / times)), times)


def total_n_interest(base=100, rate=0.01, years=1):
    '''
    计算第n年的本息
    :param base: 投入基数
    :param rate: 循环利率
    :param years: 第n年
    :return:
    '''
    if years == 1:
        return base * rate
    else:
        return total_n_interest(base * rate, rate, years - 1)


if __name__ == "__main__":
    base = 100
    rate = 0.05
    times = 12
    years = 10

    circle_rate = circle_rate(rate, times)

    # 当前利率下，一个周期所能达到的最大收益率（自然数的基准收益率幂）
    cal_by_e = math.pow(math.e, rate)
    print("当前基准利率下，最大化切分计息次数所能达到的最大利率={0}".format("{:.4%}".format(cal_by_e)))

    print("本息率={2}, 基准利率={0}, 周期内计息次数={1}".format("{:.2%}".format(rate), times, "{:.6%}".format(circle_rate)))
    for year in range(1, years + 1):
        year_interest = total_n_interest(base, circle_rate, year)
        print("第{0}个周期末累计本息和={1}".format(year, "{:.4f}".format(year_interest)))
