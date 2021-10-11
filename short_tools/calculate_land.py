# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
贷款计算
'''

import numpy as np


def equal_loan_payment(principal, period, arp):
    '''
    等额本息
    单月还款额计算公式： A * β * (1 + β) ^ k / [(1 + β) ^ k - 1]
    当月应还利息： A * β * [(1 + β) ^ k - (1 + β) ^ (n - 1)] /[(1 + β) ^ k - 1]
    当月应还本金： A * β * (1 + β) ^ (n - 1) / [(1 + β) ^ k - 1]
    :param principal: 贷款金额
    :param period: 还款期数
    :param arp: 年化利率
    :return:
    '''
    monthly_rate = np.round(arp / 12, 4)
    monthly_amount = np.divide(principal * monthly_rate * np.power(1 + monthly_rate, period),
                               (np.power(1 + monthly_rate, period) - 1))
    monthly_amount = np.round(monthly_amount, 2)
    total_amount = monthly_amount * period
    cumulative_interest = 0
    cumulative_principal = 0
    print("*" * 30)
    print("等额本息")
    print(f"借款总额={principal},还贷总期数={period},年化利率={arp*100}%,总还款={total_amount}")
    for n in range(1, period + 1):
        # 每月应还利息
        monthly_interest = np.divide(principal * monthly_rate * (np.power(1 + monthly_rate, period) - np.power(1 + monthly_rate, (n - 1))),
                                     (np.power(1 + monthly_rate, period) - 1))
        monthly_interest = np.round(monthly_interest, 2)
        cumulative_interest = np.round(cumulative_interest + monthly_interest, 2)

        # 每月应还本金
        monthly_principal = np.divide(principal * monthly_rate * np.power(1 + monthly_rate, (n - 1)),
                                      (np.power(1 + monthly_rate, period) - 1))
        monthly_principal = np.round(monthly_principal, 2)
        cumulative_principal = np.round(cumulative_principal + monthly_principal, 2)
        print(f"第{n}期:还款={monthly_amount},本金={monthly_principal},利息={monthly_interest}"
              f"\t累计本金={cumulative_principal},累计利息={cumulative_interest},"
              f"累计本息={np.round(cumulative_principal + cumulative_interest, 2)}")


def equal_principal_payment(principal, period, arp):
    '''
    等额本金
    当月利息： (A-已还款额) * β
    当月本金： A / k
    :param principal: 贷款金额
    :param period: 还款期数
    :param arp: 年化利率
    :return:
    '''
    monthly_rate = np.round(arp / 12, 4)
    monthly_principal = np.round(principal / period, 2)
    cumulative_interest = 0
    cumulative_principal = 0
    print("*" * 30)
    print("等额本金")
    print(f"借款总额={principal},还贷总期数={period},年化利率={arp * 100}%")
    for n in range(1, period + 1):
        monthly_interest = np.round((principal - cumulative_principal) * monthly_rate, 2)
        cumulative_principal = np.round(cumulative_principal + monthly_principal, 2)
        cumulative_interest = np.round(cumulative_interest + monthly_interest, 2)
        monthly_amount = np.round(monthly_principal + monthly_interest, 2)
        print(f"第{n}期:还款={monthly_amount},本金={monthly_principal},利息={monthly_interest}"
              f"\t累计本金={cumulative_principal},累计利息={cumulative_interest},"
              f"累计本息={np.round(cumulative_principal + cumulative_interest, 2)}")


if __name__ == '__main__':
    # 等额本息
    principal = 1320000
    period = 360
    arp = 0.0588
    equal_loan_payment(principal, period, arp)

    principal = 950000
    period = 348
    arp = 0.0588
    equal_loan_payment(principal, period, arp)

    principal = 950000
    period = 200
    arp = 0.0588
    equal_loan_payment(principal, period, arp)

    equal_principal_payment(principal, period, arp)
