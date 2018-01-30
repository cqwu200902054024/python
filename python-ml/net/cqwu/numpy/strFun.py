#-*-coding:utf-8-*-
"""
numPy - 字符串函数
    以下函数用于对dtype为numpy.string_或numpy.unicode_的数组执行向量化字符串操作。 它们基于 Python 内置库中的标准字符串函数
    1. 	add() 返回两个str或Unicode数组的逐个字符串连接
    2. 	multiply() 返回按元素多重连接后的字符串
    3. 	center() 返回给定字符串的副本，其中元素位于特定字符串的中央
    4. 	capitalize() 返回给定字符串的副本，其中只有第一个字符串大写
    5. 	title() 返回字符串或 Unicode 的按元素标题转换版本
    6. 	lower() 返回一个数组，其元素转换为小写
    7. 	upper() 返回一个数组，其元素转换为大写
    8. 	split() 返回字符串中的单词列表，并使用分隔符来分割
    9. 	splitlines() 返回元素中的行列表，以换行符分割
    10. 	strip() 返回数组副本，其中元素移除了开头或者结尾处的特定字符
    11. 	join() 返回一个字符串，它是序列中字符串的连接
    12. 	replace() 返回字符串的副本，其中所有子字符串的出现位置都被新字符串取代
    13. 	decode() 按元素调用str.decode
    14. 	encode() 按元素调用str.encode
"""
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')
if __name__ == '__main__':
    #numpy.char.add()函数执行按元素的字符串连接。
    astr1 = np.array([[1,2,3,4],[1,2,3,4]],dtype='str')
    print astr1
    astr2 = np.array([[1,2,3,4],[1,2,3,4]],dtype='str')
    print "np.char.add:"
    print np.char.add(astr1,astr2)
    astr3 = np.array([1,2,3,4],dtype='str')
    print "add:"
    #不能广播
    #print np.char.add(astr2 + astr3)
    #numpy.char.multiply()多重连接
    print np.char.multiply('str',4)
    #numpy.char.center()返回所需宽度的数组，以便输入字符串位于中心，并使用fillchar在左侧和右侧进行填充
    c = np.char.center('hello',20,fillchar='1')
    print c
    c = np.char.center(np.array([[1,2],[3,4]],dtype='str'),4,fillchar='0')
    print c
    #umpy.char.capitalize()返回字符串的副本，其中第一个字母大写
    c = np.char.capitalize(np.array(['abv','cdf']))
    print c
    #numpy.char.title()返回输入字符串的按元素标题转换版本，其中每个单词的首字母都大写。
    print np.char.title('hello how are you')
    #numpy.char.lower()函数返回一个数组，其元素转换为小写。它对每个元素调用str.lower。
    print np.char.lower(['HELLO','WORLD'])
    print np.char.lower('HELLO')
    #numpy.char.upper()函数返回一个数组，其元素转换为大写。它对每个元素调用str.upper。
    print np.char.upper('hello')
    print np.char.upper(['hello','world'])
    #numpy.char.split()返回输入字符串中的单词列表。 默认情况下，空格用作分隔符。 否则，指定的分隔符字符用于分割字符串。
    print np.char.split('hello are you')
    print np.char.split('ni,hao,ma',sep=',')
    #numpy.char.splitlines()函数返回数组中元素的单词列表，以换行符分割。
    print np.char.splitlines('hello\nhow are you')
    #numpy.char.strip()函数返回数组的副本，其中元素移除了开头或结尾处的特定字符。
    print np.char.strip('qsdsddsdsaq','q')
    print np.char.strip(['sdsds'],'s')
    #numpy.char.join()返回一个字符串，其中单个字符由特定的分隔符连接。
    print np.char.join('-','CHINA')
    print np.char.join(['-','*'],['zp','st'])
    #numpy.char.replace()返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代。
    print np.char.replace('zhssang psseng','ss','')
    #numpy.char.decode()在给定的字符串中使用特定编码调用str.decode()
    print np.char.decode(np.char.encode('张朋','utf-8'),'utf-8')
















