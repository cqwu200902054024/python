#-*-coding:utf-8 -*-
"""
NumPy - 数组操作
NumPy包中有几个例程用于处理ndarray对象中的元素。 它们可以分为以下类型：
1. 	reshape 不改变数据的条件下修改形状
2. 	flat 数组上的一维迭代器
3. 	flatten 返回折叠为一维的数组副本
4. 	ravel 返回连续的展开数组
"""
import numpy as np
if __name__ == '__main__':
    """
    numpy.reshape
    这个函数在不改变数据的条件下修改形状，它接受如下参数：
    numpy.reshape(arr, newshape, order')
    其中：
        arr：要修改形状的数组
        newshape：整数或者整数数组，新的形状应当兼容原有形状
        order：'C'为 C 风格顺序，'F'为 F 风格顺序，'A'为保留原顺序。
    """
    a = np.arange(8)
    print a
    b = a.reshape(4,2)
    print a
    print b
    """
    numpy.ndarray.flat
    该函数返回数组上的一维迭代器，行为类似 Python 内建的迭代器。
    """
    # 返回展开数组中的下标的对应元素
    a = np.arange(8).reshape(4,2)
    print a
    print a.flat[5]
    """
    numpy.ndarray.flatten
    该函数返回折叠为一维的数组副本，函数接受下列参数：
    ndarray.flatten(order)
    Python
    其中：
        order：'C' — 按行，'F' — 按列，'A' — 原顺序，'k' — 元素在内存中的出现顺序。
    """
    a = np.arange(8).reshape(2,4)
    print a.flatten()
    """
    numpy.ravel
这个函数返回展开的一维数组，并且按需生成副本。返回的数组和输入数组拥有相同数据类型。这个函数接受两个参数。

numpy.ravel(a, order)
Python

构造器接受下列参数：

    order：'C' — 按行，'F' — 按列，'A' — 原顺序，'k' — 元素在内存中的出现顺序。
    """

