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



def yunsuanfu():
    """
    计算两个以上对象
    :return:
    """
    #赋值运算符
    a = 10
    b = 3
    a += b
    a -= b
    a *= b
    #逻辑运算符
    res = a and b
    res = a or b
    res =  not b

    #闰年判断
    year = int(input("请输入年份："))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year}是闰年")

def fenzhi():
    """
    经常使用，判断，结构逻辑
    :return:
    """
    #if语句的使用，用户登录判断
    name = "tom"
    passwd = "123"
    input_name = input("请输入姓名：")
    input_pwd = input("请输入密码：")
    if input_name == name and input_pwd == passwd:
        print("登录成功！")
    else:
        print("用户名或者密码不对！")

def xunhuan():
    """
    连续不断的做一件事情，就是循环
    :return:
    """
    #100内的求和，for循环演示
    s = 0
    for i in range(101):
        s += i
    print(s)
    """
    range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101。
    range(1, 101)`：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
    range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
    range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
    """
    #猜数字游戏，while循环，注意别写死循环即可
    import random
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')



def prictice():
    """
    练习1：输入一个正整数判断是不是素数。素数指的是只能被1和自身整除的大于1的整数。
    """
    from math import sqrt
    num = input("请输入一个正整数：")
    n = int(num)

    if n == 1:
        return False
    for i in range(2, int(sqrt(n) + 1)): #开平方减少计算量
        if n % i == 0:
            return False
    return True

    """
    练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
    两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
    """
    x = int(input('x = '))
    y = int(input('y = '))
    # 如果x大于y就交换x和y的值
    if x > y:
        # 通过下面的操作将y的值赋给x, 将x的值赋给y
        x, y = y, x
    # 从两个数中较小的数开始做递减的循环
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break
    """
    练习3：打印三角形
    
    """
    for i in range(13):
        for _ in range(13 - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()

    """
    练习4：求水仙花数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
    例如：$1^3 + 5^3+ 3^3=153$
    """
    for i in range(100,1000):
        big = i // 100
        middle = i // 10 %10
        min = i %10
        if i == big ** 3 + middle **3 + min **3:
            print(i)

    """
    练习4：百钱百鸡问题。公鸡5元一只，母鸡3元一只，小鸡1元三只，
    用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
    """
    for x in range(20):
        for y in range(33):
            z = 100 -x - y
            if 5*x + 3 *y + z/3 == 100:
                print(x, y, z)

    """
    练习5：赌博游戏，玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
                    玩家第一次如果摇出2点、3点或12点，庄家胜；
                    其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
    Craps赌博游戏
    我们设定玩家开始游戏时有1000元的赌注
    游戏结束的条件是玩家输光所有的赌注
    """
    from random import randint

    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')

    """
    练习6：生成**斐波那契数列**的前20个数。
    quot;。斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
    形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
    """
    num1, num2 = 0,1
    stop = int(input("请输入终止数字："))

    while num2 < stop:
        num1,num2 = num2,num1 + num2
        print(num2,end=",")


def hanshu():
    """
    代码复用，封装后便于调用
    :return:
    """
def mokuai():
    """
    把很多方法，封装到一个文件中
    比如当前文件就是一个模块
    :return:
    """

if __name__ == '__main__':
    #调用函数名字即可，例如：
    hanshu()







