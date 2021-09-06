# -*- coding: utf8 -*-
__author__ = 'wangqiang'

if __name__ == "__main__":

    base_age = 35
    # 初始投入资金
    base_count = 300000
    # 年化收益率
    yearly_income_ratio = 0.05

    # 年末追加资金初始值(单位与base_count保持一致)
    base_addition = 50000
    # 每年末追加资金上升比例
    additional_increment_ratio = 0.05

    # 投资总年数
    total_years = 30

    # 计算公式
    print("计算公式：年初资金量 * (1+年化收益率%) + 年末追加资金量 * (1+追加资金增长率%)")
    for year in range(0, total_years + 1):

        current_base = base_count
        if year > 0:
            base_age += 1
            # 从y1年开始，资金量变化包含年化增长率加上追加资金数
            base_count = current_base * (1 + yearly_income_ratio) + base_addition
            print("第%d年(%d岁): %d * (1+%.1f%%) + %d * (1+%.1f%%) = %d"
                  % (year, base_age, current_base, yearly_income_ratio * 100,
                     base_addition, additional_increment_ratio * 100, base_count))
        else:
            # y0年仅计算追加资金数
            base_count = current_base + base_addition
            print("第%d年(不计算年化增长)(%d岁): %d + %d = %d"
                  % (year, base_age, current_base, base_addition, base_count))

        # 调整下一年的追加资金数
        base_addition = base_addition * (1 + additional_increment_ratio)
