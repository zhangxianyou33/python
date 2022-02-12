#学习捷径：多练多练多练


def beijing_jieshao():
    """
    背景介绍，百度去吧
    :return:
    """

def an_zhuang():
    """
    安装介绍，百度去吧
    :return:
    """

def chakan_banben():
    """
    查看版本
    :return:
    """
    import sys
    print(sys.version_info)
    print(sys.version)


def first_code():
    """
    第一行代码 hello word
    :return:
    """
    print("hello word")
    print('hello, world!')
    # print("你好,世界！")
    print('你好', '世界')
    print('hello', 'world', sep=', ', end='!')
    print('goodbye, world', end='!\n')


def zhu_shi():
    """
    1. 单行注释 - 以#和空格开头的部分
    2. 多行注释 - 三个引号开头，三个引号结尾
    :return:
    """
    print("hello word")
    #print("hello word")
    """print('hello word')"""


def python_this():
    """
    python之禅，看个开心就好
    :return:
    """
    print("python之禅")
    import this

    print("画个正方形")
    import turtle
    turtle.pensize(4)
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.mainloop()


def bian_liang():
    """
    变量就是一个名字，就像你的名字代表你这个人，说明一个对象
    :return:
    """
    name = "tom"
    age = 22

def lei_xing():
    """
    python的基础类型
    :return:
    """
    age = 22     #整型
    score = 99.9 #浮点型
    name = "张三" #字符型
    a = True     #布尔型，只有True和False ，可以用0 和1 代表
    num = 3 + 5j #负数型

    #类型互相转换
    age = 22
    float_age = float(age)
    int_age = int(float_age)
    str_age = str(int_age)
    """
    int()`：将一个数值或字符串转换成整数，可以指定进制。
    float()`：将一个字符串转换成浮点数。
    str()`：将指定的对象转换成字符串形式，可以指定编码。
    chr()`：将整数转换成该编码对应的字符串（一个字符）。
    ord()`：将字符串（一个字符）转换成对应的编码（整数
    """

    #闰年判断
    year = int(input("请输入年份："))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year}是闰年")

def yunsuanfu():
    pass

