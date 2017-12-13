#-*- coding: UTF-8 -*-
if __name__ == '__main__':
    """
    Python不支持单字符类型，单字符也在Python也是作为一个字符串使用。
    Python访问子字符串，可以使用方括号来截取字符串
    """
    var1 = 'hello python'
    var2 = "hello Runoob"
    print var1[0]
    print var2[1:5]
    #对已存在的字符串进行修改，并赋值给另一个变量
    print var1[:6] + "Runoob"
    """
    r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，
    没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，
    与普通字符串有着几乎完全相同的语法。
    """
    #字符串格式化
    print "My name is %s,my age is %d" % ('zhangpeng',32)
    print u'中国'
    list = [1,'zp',3.24,"hello"]
    list[0] = "peng"
    print list
    print len(list)
    print list + [3,4,5,6]
    list.append("heoow")
    print list
    """
    元组中只包含一个元素时，需要在元素后面添加逗号
    任意无符号的对象，以逗号隔开，默认为元组，如下实
    """
    tuple = ("zp",)
    print tuple
    """
    1）不允许同一个键出现两次。
    2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
    """
    dict = {'Name' : 'Zara','Age' : 32,'Class' : 'Frist'}
    print dict['Name']
    print dict.get('Name')
    dict['Lang'] = 'Python'
    print dict
    dict['Class'] = 'Cqwu'
    print dict
    del dict['Lang']
    print dict
    print '==='
    dict.clear()
    print dict
    """
    Python 日期和时间
    很多Python函数用一个元组装起来的9组数字处理时间:
    也就是struct_time元组。
    time.struct_time(tm_year=2017, tm_mon=12, tm_mday=13, tm_hour=13, tm_min=54, tm_sec=6, tm_wday=2, tm_yday=347, tm_isdst=0)
    """
    import time
    print time.time()
    #获取时间元组
    localTime =  time.localtime(time.time())
    print localTime
    #获取格式化的时间
    lt = time.asctime(localTime)
    print lt
    #使用 time 模块的 strftime 方法来格式化日期
    print time.strftime("%Y-%m-%d",localTime)
    #获取某月日历
    import calendar
    cal = calendar.month(2017,12)
    print cal