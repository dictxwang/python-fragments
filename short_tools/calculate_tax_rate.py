# -*- coding: utf8 -*-
# created at 2020/3/7
__author__ = 'wangqiang'

# 月薪
monthly_salary = 42000
# 附加专项扣除（房贷+赡养老人）
monthly_extra_takeoff = 1000 + 1000
# 特定月份实际薪资
monthly_salary_actual = {
    # 1: 20863.8,
    # 2: 20836.9,
    # 3: 20836.9 + 20298,
    # 4: 20836.9 + 22950,
    # 7: 20836.9 + 22950,
    # 8: 20836.9,
    # 10: 20836.9 + 22950,
    # 11: 20836.9
}
# 税率起征点
monthly_tax_threshold = 5000
# 每月社保公积金
monthly_social_fund = 4262.62
# 特定月份实际社保公积金
monthly_social_fund_actual = {
    # 1: 4500.22,
    # 2: 4500.22,
    # 3: 4500.22,
    # 4: 4500.22,
    # 5: 4500.22,
    # 6: 4500.22,
}
# 年度税率点
yearly_tax_rate_sheet = [
    # (下限，上限，税率，速扣数)
    (0, 36000, 3, 0),
    (36000, 144000, 10, 2520),
    (144000, 300000, 20, 16920),
    (300000, 420000, 25, 31920),
    (420000, 660000, 30, 52920),
    (660000, 960000, 35, 85920),
    (960000, 100000000, 45, 181920)
]

# 年终奖税率表（用总额除以12个月，看落到那个区间，在用所在区间的税率和速算扣除数对总额进行计算）
# 年终奖分为合并计税和单独计税两种方式
year_end_tax_rate_sheet = [
    (0, 3000, 3, 0),
    (3000, 12000, 10, 210),
    (12000, 25000, 20, 1410),
    (25000, 35000, 25, 2660),
    (35000, 55000, 30, 4410),
    (55000, 80000, 35, 7160),
    (80000, 10000000, 45, 15160)
]

'''
速扣数计算方式：
第1级数，速算扣除是0
第2级数，速算扣除是36000×（10%-3%）=2520
第3级数，速算扣除是144000×（20%-10%）+2520=16920
第4级数，速算扣除是300000×（25%-20%）+16920=31920
第5级数，速算扣除是420000×（30%-25%）+31920=52920
第6级数，速算扣除是660000×（35%-30%）+52920=85920
第7级数，速算扣除是960000×（45%-35%）+85920=181920
'''

if __name__ == "__main__":

    total_salary = 0.0
    total_social_fund = 0.0
    total_extra_takeoff = 0.0
    total_basic_takeoff = 0.0
    total_tax = 0.0

    for month in range(1, 13):
        if month in monthly_salary_actual:
            current_salary = monthly_salary_actual[month]
        else:
            current_salary = monthly_salary
        if month in monthly_social_fund_actual:
            total_social_fund += monthly_social_fund_actual[month]
        else:
            total_social_fund += monthly_social_fund
        total_salary += current_salary
        total_extra_takeoff += monthly_extra_takeoff
        total_basic_takeoff += monthly_tax_threshold

        current_tax_rate = None
        for tax_rate in yearly_tax_rate_sheet:
            after_takeof = total_salary - total_social_fund - total_extra_takeoff
            if tax_rate[0] < after_takeof <= tax_rate[1]:
                current_tax_rate = tax_rate
                break

        current_tax = (total_salary - total_social_fund - total_extra_takeoff - total_basic_takeoff) \
                      * current_tax_rate[2] / 100 - current_tax_rate[3] - total_tax

        print("%d:[(%.2f-%.2f-%d-%d)*%s-%d]-%.2f=%.2f" % (month, total_salary, total_social_fund, total_extra_takeoff,
                                                 total_basic_takeoff, str(current_tax_rate[2]) + "%",
                                                 current_tax_rate[3], total_tax, current_tax))
        total_tax += current_tax
    print("job finished. yearly total tax: %.2f" % total_tax)
