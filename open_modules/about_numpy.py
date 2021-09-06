# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip install numpy
'''

import numpy as np


def test_array():
    '''
    有关narray的使用，narray是numpy库的基础和核心
    :return:
    '''
    print("> test_array")
    # 创建array
    na1 = np.array([1, 3, 5])
    # int64
    print(na1.dtype)
    na2 = np.array([[1, 3, 5], [2, 4, 6]], dtype="int16")
    # int 16
    print(na2.dtype)
    # 可以将列表和元组一起使用
    na3 = np.array([[1, 3, 5], (2, 4, 6)])
    # 维度是2
    print(na3.ndim)

    na4 = np.array(['a', 'b', 'c'])
    # <U1  默认字符类型元素
    print(na4.dtype)
    na5 = np.array(['a', 'b', 'c'], dtype='S1')
    # |S1
    print(na5.dtype)

    # 自动转换为复数形式
    na6 = np.array([1, 3, 5], dtype=complex)
    # [1.+0.j 3.+0.j 5.+0.j]
    print(na6)

    # 通过arange用指定区间的元素生成矩阵
    na7 = np.arange(0, 5)
    # [0 1 2 3 4]
    print(na7)
    na8 = np.arange(0, 12, 3)
    # [0 3 6 9]
    print(na8)
    # 生成3*4矩阵
    na9 = np.arange(0, 12).reshape(3, 4)
    print(na9)
    # 使用linspace将区间分为指定份数
    na10 = np.linspace(0, 10, 5, dtype=int)
    # [ 0  2  5  7 10]
    print(na10)

    # 使用random生成随机数矩阵
    na11 = np.random.random(3)
    print(na11)
    # 生成3*3随机数矩阵
    na12 = np.random.random((3, 3))
    print(na12)

    # 全零矩阵和单位矩阵
    na13 = np.zeros((3, 3), dtype=int)
    # 3*3全零矩阵，dtype默认是float64
    print(na13)
    na14 = np.ones((2, 2))
    # 2*2单位矩阵
    print(na14)


def test_operation():
    '''
    测试基本操作
    :return:
    '''
    print("> test_operation")
    # 元素级加减乘除
    na1 = np.arange(0, 5)
    # [2 3 4 5 6]
    print(na1 + 2)
    # [-2 -1  0  1  2]
    print(na1 - 2)
    # [0 0 1 1 2]
    print(na1 // 2)
    # [0 2 4 6 8]
    print(na1 * 2)

    a = np.arange(0, 3)
    b = np.arange(6, 9)
    # [ 6  8 10]
    print(a + b)
    # [-6 -6 -6]
    print(a - b)
    # [ 0  7 16] 元素间相乘，非矩阵相乘
    print(a * b)
    # [0 0 0] 元素间相除
    print(a // b)
    # 与函数结果相乘
    print(a * np.sin(b))


def test_dot():
    '''
    矩阵积（矩阵乘法）
    :return:
    '''
    print("> test_dot")
    a = np.arange(1, 5)
    b = np.arange(5, 9)
    # 70
    print(a.dot(b))

    a = np.arange(1, 10).reshape(3, 3)
    b = np.arange(11, 20).reshape(3, 3)
    # 结果仍然是3*3矩阵
    print(a.dot(b))
    # 矩阵乘法不满足交换律
    print(b.dot(a))


def test_function():
    '''
    测试通用函数，通用函数（universal function）通常叫作ufunc
    :return:
    '''
    print("> test_function")
    na1 = np.arange(1, 4)
    # 平方根
    print(np.sqrt(na1))
    # 幂运算
    print(np.power(na1, 2))
    # 对数运算
    print(np.log(na1))
    print(np.log10(na1))
    print(np.log2(na1))
    # 三角运算
    print(np.sin(na1))
    print(np.tan(na1))
    print(np.cos(na1))
    print(np.arctan(na1))

    # 聚合函数
    print(np.sum(na1))
    print(np.mean(na1))
    print(np.min(na1))
    print(np.max(na1))
    # 计算标准差
    print(np.std(na1))

    na2 = np.arange(1, 10).reshape(3, 3)
    # 9
    print(np.max(na2))


def test_index():
    '''
    索引与切片
    :return:
    '''
    print("> test_index")
    na1 = np.arange(1, 10)
    # 1
    print(na1[0])
    # [1 3] 返回多个元素
    print(na1[[0, 2]])
    na2 = na1.reshape(3, 3)
    # 1
    print(na2[0, 0])

    na3 = np.arange(1, 10)
    # [2 4 6] 从下标1到6 切片，间隔2
    na3_c1 = na3[1:6:2]
    print(na3_c1)

    na4 = na3.reshape(3, 3)
    # 行列都从0~2切片
    na4_c1 = na4[0:2, 0:2]
    print(na4_c1)


def test_sharp_change():
    '''
    变形测试
    :return:
    '''
    print("> test_sharp_change")
    # flatten 和 ravel的区别在于flatten是拷贝，而ravel是视图
    na = np.arange(1, 10).reshape(3, 3)
    na_flat = na.flatten()
    print(na_flat)
    # 拷贝的元素改变不影响原数组
    na_flat[1] = 123
    print(na)

    na_ravel = na.ravel()
    print(na_ravel)
    # 视图的元素改变会影响原数组
    na_ravel[1] = 123
    print(na)


def test_broadcasting():
    print("> test_broadcasting")
    na1 = np.arange(1, 10).reshape(3, 3)
    # 返回和na1形状一样的全1数组
    na2 = np.ones_like(na1)
    print(na2)
    # 返回和na1形状一样的全0数组
    na3 = np.zeros_like(na1)
    print(na3)

    na4 = np.array([1, 2, 3, 4])
    # 广播，重复na4的各个维度，行*3次，列*1
    na5 = np.tile(na4, (3, 1))
    print(na5)

    na6_1 = np.arange(1, 7).reshape(2, 3)
    print(na6_1)
    na6_2 = np.arange(0, 3)
    print(na6_2)
    # 具有相同的列数，可以广播
    print(na6_1 + na6_2)

    na6_3 = np.arange(0, 2).reshape(2, 1)
    print(na6_3)
    # 具有相同的行数，可以广播
    print(na6_1 + na6_3)

    na6_4 = np.arange(1, 2)
    # 单个数字，可以广播
    print(na6_1 + na6_4)

    na6_5 = np.arange(1, 5).reshape(2, 2)
    # 行数相同但是列数不同，不能广播
    # print(na6_1 + na6_5)
    na6_6 = np.arange(1, 7).reshape(3, 2)
    # 行列数都不同，不能广播
    # print(na6_1 + na6_6)



def test_sort():
    '''
    排序相关
    :return:
    '''
    lst = [3, 1, 0, 2, 1, 10, 12]
    # 默认是quicksort
    lst1 = np.sort(lst, kind="quicksort")
    print(lst1)
    lst2 = np.sort(lst, kind="mergesort")
    print(lst2)
    lst3 = np.sort(lst, kind="heapsort")
    print(lst3)


def test_matrix():
    '''
    矩阵相关
    :return:
    '''
    print("> test_matrix")
    na1 = np.arange(1, 10).reshape(3, 3)
    # 矩阵行列转置
    print(na1.T)
    # 矩阵行列转置
    print(np.transpose(na1))

    # 返回2*2的随机数矩阵
    m1 = np.empty((2, 2))
    # <class 'numpy.matrix'>
    print(type(m1))
    print(m1)
    m2 = np.ones((2, 3), dtype=int)
    print(m2)
    m3 = np.zeros((3, 2))
    print(m3)
    # 返回对角矩阵（行数，列数，对角线索引）
    m4 = np.eye(N=4, M=3, k=0)
    print(m4)
    # 返回单位矩阵
    m5 = np.identity(4)
    print(m5)


def test_lianlg():
    '''
    线性代数相关
    :return:
    '''
    print("> test_lianlg")
    m1 = np.arange(1, 10).reshape(3, 3)
    m2 = np.arange(11, 20).reshape(3, 3)
    # 矩阵相乘
    print(np.dot(m1, m2))
    # 向量点积，自动展开
    # 735
    print(np.vdot(m1, m2))
    # 內积
    print(np.inner(m1, m2))
    # 乘积 matmul和dot都可以进行矩阵乘法计算
    print(np.matmul(m1, m2))
    # 求解齐次方程组
    a = np.array([[8, -6, 2], [-4, 11, -7], [4, -7, 6]])
    b = np.array([[28], [-40], [33]])
    x = np.linalg.solve(a, b)
    print(x)

    # allclose判断两个数组的所有元素是否相同
    print(np.allclose(np.dot(a, x), b))
    # 求解方阵的逆矩阵
    at = np.linalg.inv(a)
    print(at)
    # 方阵a与其逆矩阵相乘，结果是单位矩阵
    print(a.dot(at))
    # 通过逆矩阵求解联立方程组
    x1 = at.dot(b)
    print(x1)
    # True
    print(np.allclose(x1, x))

    # 伴随矩阵，通过求解逆矩阵的公式来 A逆矩阵=(1/A的行列式|A|)*A的伴随矩阵
    x2 = np.array([[8, -6, 2], [-4, 11, -7], [4, -7, 6]])
    print(x2)
    # 求逆矩阵
    x2t = np.linalg.inv(x2)
    print(x2t)
    # 求行列式
    x2det = np.linalg.det(x2)
    print(x2det)
    # 求伴随矩阵
    x2to = x2t * x2det
    print(x2to)

    # x3是正交矩阵，正交矩阵的转置和其逆矩阵相同
    x3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    print(np.linalg.inv(x3))
    print(x3.T)

    x4 = np.array([[1, 2], [3, 4]])
    x4_ext = np.array([[1, 2, 1, 0], [3, 4, 0, 1]])
    # 可以通过对增广矩阵做行的初等变换，将左侧变换成单位矩阵，则右侧即为逆矩阵
    print(x4_ext)
    print(np.linalg.inv(x4))


def test_shape_dim():
    '''
    测试形状和维度
    :return:
    '''
    print("> test_shape_dim")
    na1 = np.arange(1, 7).reshape(2, 3)
    print(na1)
    # 形状 (2, 3)
    print(na1.shape)
    # 维度 2
    print(na1.ndim)


def test_norm():
    '''
    测试范数相关
    :return:
    '''
    print("> test_norm")
    # 向量的范数
    na1 = np.array([3, 0, -4])
    # 0-范数，表示向量中非零元素的个数
    n0 = np.linalg.norm(na1, ord=0)
    print(n0)
    # 1-范数，表示向量中所有元素的绝对值之和
    n1 = np.linalg.norm(na1, ord=1)
    print(n1)
    # 2-范数，表示向量中所有元素的平方之和的平方根
    n2 = np.linalg.norm(na1, ord=2)
    print(n2)
    # 正无穷-范数，表示向量中元素绝对值的最大值
    ninf = np.linalg.norm(na1, ord=np.inf)
    print(ninf)
    # 负无穷-范数，表示向量中元素绝对值的最小值
    nninf = np.linalg.norm(na1, ord=-np.inf)
    print(nninf)

    # 矩阵的范数
    x = np.array([[-1, 1, 0], [-4, 3, 0], [1, 0, 2]])
    # 1-范数，又名列和范数 即列向量中绝对值之和的最大值
    # 6
    print(np.linalg.norm(x, ord=1))
    # 2-范数，又名谱范数 计算方法为当前矩阵转置与当前矩阵相乘的最大特征值的开平方
    xtx = np.matmul(x.T, x)
    print(xtx)
    lambda_xtx = np.linalg.eigvals(xtx)
    # [27.71086452  0.03392256  4.25521292] 其中最大特征值是 27.71086452
    print(lambda_xtx)
    # 计算特征值与特征向量
    vector_xtx = np.linalg.eig(xtx)
    print(vector_xtx)
    x_norm_2 = np.sqrt(np.max(lambda_xtx))
    # 5.264110990106892
    print(x_norm_2)
    # 5.264110990106893 一步到位计算的结果和分步计算结果一致
    print(np.linalg.norm(x, ord=2))
    # F-范数，Frobenius范数，计算方式为矩阵元素的平方和再开平方
    # 5.656854249492381
    print(np.linalg.norm(x, ord="fro"))
    # 正无穷范数，是指矩阵中行向量中绝对值之和的最大值
    # 7.0
    print(np.linalg.norm(x, ord=np.inf))

    x1 = np.array([1, 2, 3, 4]).reshape(2, 2)
    x2 = np.array([2, 4, 6, 8]).reshape(2, 2)
    # x2元素是x1的两倍，x2的特征值是x1的两倍，而两者的特征向量相同
    print(np.linalg.eig(x1))
    print(np.linalg.eig(x2))


def my_test():
    x1 = np.array([[1, 2], [3, 4]])
    x2 = np.array([[1, 2], [-3, -4]])
    print(np.linalg.eig(x1))
    print(np.linalg.eig(x2))


if __name__ == "__main__":

    # test_array()
    # test_operation()
    # test_dot()
    # test_function()
    # test_index()
    # test_sharp_change()
    # test_broadcasting()
    # test_sort()
    # test_matrix()
    # test_lianlg()
    # test_shape_dim()
    # test_norm()

    my_test()
