# -*- coding: UTF-8 -*-
"""
Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
"""
if __name__ == '__main__':
    """
    Python 标识符
    在 Python 里，标识符由字母、数字、下划线组成。
    在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
    Python 中的标识符是区分大小写的。
    以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
    以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
    """
    '''
   变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
   基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
   因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。
   Python 中的变量赋值不需要类型声明。
   每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
   每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
    '''
    counter = 100
    miles = 1000.0
    name = "hohe"
    print counter,miles,name
    """
    Python有五个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
    """
    #他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
    var1 = 1
    var2 = 2
    #以使用del语句删除一些对象的引用
    del var2
    #print var2  #name 'var2' is not defined

    """
    python的字串列表有2种取值顺序:
    从左到右索引默认0开始的，最大范围是字符串长度少1
    从右到左索引默认-1开始的，最大范围是字符串开头
    """
    s = "zhangpeng"
    print s[1:]
    print s[-3:-1]
    #加号（+）是字符串连接运算符，星号（*）是重复操作
    str = 'hello word'
    print str * 2
    """
    列表用 [ ] 标识，是 python 最通用的复合数据类型。
    列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，
    从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
    """
    list = ['runoob',123,'23.4']
    tinyList = [456,'jone']
    print list[0]
    print list + tinyList
    """
    元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
    """
    tuple = ('runoob',783,'jone')
    tinyTupe = (123,12.3)
    print tuple[0]
    print tuple[1:3]
    print tuple + tinyTupe
    #'tuple' object does not support item assignment
    #tuple[0] = 1
    """
    列表是有序的对象集合，字典是无序的对象集合。
    两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
    字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
    """
    dict = {}
    dict['one'] = 'this is one'
    dict[2] = 'this is two'
    tinyDict = {'name': 'john','code' : 123,'dept' : 'sales'}
    print dict[2]
    print dict
    print dict.get(2)
    print tinyDict.keys()
    print tinyDict.values()
    """
    我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
     int(x [,base])
     将x转换为一个整数
     long(x [,base] )
     将x转换为一个长整数
     float(x)
     将x转换到一个浮点数
     complex(real [,imag])
     创建一个复数
     str(x)
     将对象 x 转换为字符串
     repr(x)
     将对象 x 转换为表达式字符串
     eval(str)
     用来计算在字符串中的有效Python表达式,并返回一个对象
     tuple(s)
     将序列 s 转换为一个元组
     list(s)
     将序列 s 转换为一个列表
     set(s)
     转换为可变集合
     dict(d)
     创建一个字典。d 必须是一个序列 (key,value)元组。
    """
    """
    Python逻辑运算符:
    and or not
    Python成员运算符:
    in   not in
    Python身份运算符
    is is not
    is 是判断两个标识符是不是引用自一个对象
    is not 是判断两个标识符是不是引用自不同对象
    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
    """
    a = 10
    b = 20
    c = 20
    print a in list
    print b not in list
    print a is c
    print b is c
    """
    Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
    当判断条件为多个值时，可以使用以下形式：
    if 判断条件1:
        执行语句1……
    elif 判断条件2:
        执行语句2……
    elif 判断条件3:
        执行语句3……
    else:
        执行语句4……
    """
    flag = False
    name = 'luren'
    num = 9
    if num >= 0 and num <= 10:
        print 'hello'
    else:
        print 'sb'
    count = 0
    while count < 5:
        print count
        count += 1
    else:
         print count, " is not less than 5"
    fg = 1
    #while fg:print 'test'
    """
    在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）
    的情况下执行，while … else 也是一样。
    """
    for num in range(10,20):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print num




