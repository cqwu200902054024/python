#-*-coding:utf-8-*-
"""
NumPy - 数组上的迭代
NumPy 包包含一个迭代器对象numpy.nditer。 它是一个有效的多维迭代器对象，可以用于在数组上进行迭代。 数组的每个元素可使用 Python 的标准Iterator接口来访问。
让我们使用arange()函数创建一个 3X4 数组，并使用nditer对它进行迭代。
"""
import numpy as np
if __name__ == "__main__":
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print a
    for x in np.nditer(a):
        print x,
    """
    迭代的顺序匹配数组的内容布局，而不考虑特定的排序。 这可以通过迭代上述数组的转置来看到。
    """
    print
    b = a.T
    print b
    for x in np.nditer(b):
        print x,

    """
    nditer对象有另一个可选参数op_flags。 其默认值为只读，但可以设置为读写或只写模式。 这将允许使用此迭代器修改数组元素。
    """
    print
    print a
    for x in np.nditer(a,op_flags = ['readwrite']):
        x[...] = 2 * x
    print a
    print "==='C', 'F', 'A', or 'K'"
    for x in np.nditer(a,flags = ['external_loop'],order = 'F'):
        print x
    """
    如果两个数组是可广播的，nditer组合对象能够同时迭代它们。 假设数组a具有维度 3X4，并且存在维度为 1X4 的另一个数组b，则使用以下类型的迭代器(数组b被广播到a的大小)。
    """
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print a
    b = np.array([1,  2,  3,  4], dtype =  int)
    print b
    print "++++"
    for x,y in np.nditer([a,b]):
        print x,y,
        print  "%d:%d"  %  (x,y),
