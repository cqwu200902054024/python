#-*-coding:utf-8-*-
"""
    NumPy - 副本和视图
    在执行函数时，其中一些返回输入数组的副本，而另一些返回视图。 当内容物理存储在另一个位置时，称为副本。 另一方面，如果提供了相同内存内容的不同视图，我们将其称为视图。

    简单的赋值不会创建数组对象的副本。 相反，它使用原始数组的相同id()来访问它。
    一个数组的任何变化都反映在另一个数组上。 例如，一个数组的形状改变也会改变另一个数组的形状。
"""
import numpy as np
if __name__ == '__main__':
    a = np.arange(6).reshape(3,2)
    print a
    b = a
    b.shape = (2,3)
    #b的形状
    print b
    #a的形状
    print a
    print id(a)
    print id(b)
    """
    NumPy 拥有ndarray.view()方法，它是一个新的数组对象，并可查看原始数组的相同数据。 与前一种情况不同，新数组的维数更改不会更改原始数据的维数。
    """
    a = np.arange(6).reshape(2,3)
    b = a.view()
    print a
    print b
    print id(a)
    print id(b)
    b.shape = (3,2)
    print "a:"
    print a
    print "b:"
    print b
    #数组的切片也会创建视图：
    a = np.array([[10,10],  [2,3],  [4,5]])
    s = a[:,  :2]
    print s
    """
    ndarray.copy()函数创建一个深层副本。 它是数组及其数据的完整副本，不与原始数组共享。
    """
    a = np.array([[10,10],  [2,3],  [4,5]])
    b = b.copy()
    print a
    print b
    print b is a
    b[0,0] = 100
    print b
    print a


