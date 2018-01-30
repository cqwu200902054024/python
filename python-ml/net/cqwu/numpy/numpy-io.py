#-*-coding:utf-8-*-
"""
ndarray对象可以保存到磁盘文件并从磁盘文件加载。 可用的 IO 功能有：
    load()和save()函数处理 numPy 二进制文件(带npy扩展名)
    loadtxt()和savetxt()函数处理正常的文本文件
"""
import numpy as np
if __name__ == '__main__':
    a = np.array([1,2,3,4,5])
    np.save('D://outfile',a)
    b = np.load('D://outfile.npy')
    print b
    """
    save()和load()函数接受一个附加的布尔参数allow_pickles。 Python 中的pickle用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化。
    """
    a = np.array([1,2,3,4,5])
    np.savetxt('D:/out.txt',a)
    b = np.loadtxt('D:/out.txt')
    print b