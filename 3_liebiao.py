
"""
需要一个容器，用来存放东西，元素，最合适就是列表
"""
import sys


def liebiao():
    """
    列表可以存放任何元素,下标是关键特征
    :return:
    """
    list1 = [1, 3, 5, 7, 100]
    print(list1)  # [1, 3, 5, 7, 100]
    # 乘号表示列表元素的重复
    list2 = ['hello'] * 3
    print(list2)  # ['hello', 'hello', 'hello']
    # 计算列表长度(元素个数)
    print(len(list1))  # 5
    # 下标(索引)运算
    print(list1[0])  # 1
    print(list1[4])  # 100
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]

    """
    for 循环遍历列表
    """
    # 通过循环用下标遍历列表元素
    for index in range(len(list1)):
        print(list1[index])
    # 通过for循环遍历列表元素
    for i in list1:
        print(i)
    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        print(index, elem)
def fangfa():
    """
    列表的常用方法
    :return:
    """
    list1 = [1, 3, 5, 7, 100]
    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    # 合并两个列表
    list1.extend([1000, 2000])
    list1 += [1000, 2000]
    print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
    print(len(list1))  # 9
    # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
    if 3 in list1:
        list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]
    # 从指定的位置删除元素
    list1.pop(0)
    list1.pop(len(list1) - 1)
    print(list1)  # [400, 5, 7, 100, 200, 1000]
    # 清空列表元素
    list1.clear()
    print(list1)

def qiepian():
    """
    切片包头不包尾
    :return:
    """
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # apple strawberry waxberry
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

def paixu():
    """
    两种排序方法：原表不动，修改原表
    :return:
    """
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    print(list1)
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list2 = sorted(list1, reverse=True)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)
    print(list2)
def others():
    """
    生成式和生成器
    :return:
    """

    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)

    print("占用内存演示")
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    # for val in f:
    #     print(val)
"""
`yield`关键字将一个普通函数改造成生成器函数
"""
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
        yield a
def main():
    for i in fib(20):
        print(i)

if __name__ == '__main__':
    main()
