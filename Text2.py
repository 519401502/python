# coding=UTF-8
import sys




# --- 迭代式实例开始
# 生成器函数 - 斐波那契
import urllib2
from lib2to3.pgen2 import parse, parse


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        # 到这里会将 a 返回，当调用next()之后会在这里继续执行
        yield a
        a, b = b, a + b
        counter += 1


# f 是一个迭代器，由生成器返回生成

f = fibonacci(10)

while True:
    try:
        print (next(f))
    except StopIteration:
        sys.exit()

# --- 迭代器结束
o = 2


def text(x, y):
    return x * y


print text(1, 2)

# lambda 表达式
textSum = lambda i, j: i + j
print textSum(1, 2)

# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# 以下实例修改全局变量 num：
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)

fun1()

urltext = ""
urllib.urlopen(urltext)
