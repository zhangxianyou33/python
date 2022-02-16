

def str_zifuchuan():
    """
    字符串就是文字类型
    :return:
    """
    s1 = 'hello, world!'
    s2 = "hello, world!"
    # 以三个双引号或单引号开头的字符串可以折行
    s3 = """
    hello, 
    world!
    """
    print(s1, s2, s3, end='')
    """
    有些特殊字符，为了展示，需要转义符
    """
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u9a86\u660a'
    print(s1, s2)
    """
    如果不希望字符串中的`\`表示转义,最前面加上字母`r`来加以说明
    """
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='')

    """
    运算符的使用
    """
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello
    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world
    print('ll' in s1)  # True
    print('good' in s1)  # False
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45

def fangfa():
    """
    字符串的基本方法
    :return:
    """
    str1 = "hello word"
    print(len(str1))
    print(str1.capitalize())
    print(str1.title())
    print(str1.upper())
    print(str1.lower())
    print(str1.find("h"))# 找不到子串时会引发异常
    print(str1.index("h"))# 找不到子串时会引发异常
    print(str1.startswith("h"))
    print(str1.endswith("h"))
    print(str1.center(50,"="))
    print(str1.rjust(50,"="))
    print(str1.ljust(50,"="))
    print(str1.isalnum())
    print(str1.isalnum())
    print(str1.isascii())
    print(str1.isdigit())
    print(str1.islower())
    print(str1.istitle())
    print(str1.isspace())
    print(str1.isidentifier())

def geshihua():
    """
    字符串输出，指定格式输出
    %
    format
    :return:
    """
    a, b = 5, 10
    print('%d * %d = %d' % (a, b, a * b))
    print('{} * {} = {}'.format(a, b, a * b))
    print(f'{a} * {b} = {a*b}')

if __name__ == '__main__':
    geshihua()