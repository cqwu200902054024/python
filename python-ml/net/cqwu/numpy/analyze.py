#-*-coding:utf-8-*-
"""
NumPy - 统计函数
    NumPy 有很多有用的统计函数，用于从数组中给定的元素中查找最小，最大，百分标准差和方差等。

NumPy - 排序、搜索和计数函数
    NumPy中提供了各种排序相关功能。 这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。 下表显示了三种排序算法的比较。
    种类 	速度 	最坏情况 	工作空间 	稳定性
    'quicksort'(快速排序) 	1 	O(n^2) 	0 	否
    'mergesort'(归并排序) 	2 	O(n*log(n)) 	~n/2 	是
    'heapsort'(堆排序) 	3 	O(n*log(n)) 	0 	否
"""
import numpy as np

if __name__ == "__main__":
    #numpy.amin() 和 numpy.amax()这些函数从给定数组中的元素沿指定轴返回最小值和最大值。
    a = np.array([[3,7,5],[8,4,3],[2,4,9]])
    print np.amin(a,1)#返回每行最小值
    print np.amax(a,1)
    print np.amin(a,0)#返回每列最小值
    print np.amax(a,axis = 0)
    #numpy.ptp()函数返回沿轴的值的范围(最大值 - 最小值)。
    print "====="
    print np.ptp(a,1)#每行的最大值-最小值
    print np.ptp(a,axis = 0)#每列的最大值-最小值
    """
    numpy.percentile()计算分位数
    百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比。 函数numpy.percentile()接受以下参数。
    numpy.percentile(a, q, axis)
    1. 	a 输入数组
    2. 	q 要计算的百分位数，在 0 ~ 100 之间
    3. 	axis 沿着它计算百分位数的轴
    """
    a = np.array([[30,40,70],[80,20,10],[50,90,60]])
    b = a.reshape(1,9)
    print b
    print np.percentile(b,50) #中位数
    print np.percentile(a,50,axis=1)#每行的中位数
    print np.percentile(a,50,axis=0)#每列的中位数
    #numpy.median()中值定义为将数据样本的上半部分与下半部分分开的值。
    print np.median(a)
    print np.median(a,axis=1)#每行的中值
    print np.median(a,axis=0)#每列的中值
    #numpy.mean()算术平均值是沿轴的元素的总和除以元素的数量
    a = np.array([[1,2,3],[3,4,5],[4,5,6]])
    print np.mean(a,axis=1)#每行的平均值
    print np.mean(a,axis=0)#每列的平均值
    """
    numpy.average()
    加权平均值是由每个分量乘以反映其重要性的因子得到的平均值。 numpy.average()函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。 该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。
    考虑数组[1,2,3,4]和相应的权重[4,3,2,1]，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
    加权平均值 = (1*4+2*3+3*2+4*1)/(4+3+2+1)
    """
    a = np.array([1,2,3,4])
    # 不指定权重时相当于 mean 函数
    print np.average(a)
    wts = np.array([4,3,2,1])
    print np.average(a,weights=wts)
    # 如果 returned 参数设为 true，则返回权重的和
    print np.average(a,weights=wts,returned=True)
    #在多维数组中，可以指定用于计算的轴。
    a = np.arange(6).reshape(3,2)
    print a
    wts = np.array([3,5])
    print np.average(a,axis=1,weights=wts)#每行的权重平均数
    wts = np.array([2,3,5])
    print np.average(a,axis=0,weights=wts,returned=True)#每列的权重平均数
    """
    标准差
    标准差是与均值的偏差的平方的平均值的平方根。 标准差公式如下：
    std = sqrt(mean((x - x.mean())**2))
    如果数组是[1，2，3，4]，则其平均值为2.5。 因此，差的平方是[2.25,0.25,0.25,2.25]，并且其平均值的平方根除以4，即sqrt(5/4)是1.1180339887498949。
    """
    print np.std([1,2,3,4])
    #方差是偏差的平方的平均值，即mean((x - x.mean())** 2)。 换句话说，标准差是方差的平方根
    print np.var([1,2,3,4])
    """
    numpy.sort()
    sort()函数返回输入数组的排序副本。 它有以下参数：
    numpy.sort(a, axis, kind, order)
    1. 	a 要排序的数组
    2. 	axis 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
    3. 	kind 默认为'quicksort'(快速排序)
    4. 	order 如果数组包含字段，则是要排序的字段
    """
    a = np.array([[3,7],[9,1]])
    print np.sort(a,axis=1)#根据行排序
    print np.sort(a,axis=0)#按列排序
    #在 sort 函数中排序字段
    dt = np.dtype([('name',  'S10'),('age',  int)])
    a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
    print a
    print np.sort(a,order='name')#根据name排序
    #numpy.argsort()函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组。
    x = np.array([3,  1,  2])
    print np.argsort(x)
    print x[np.argsort(x)]


