import sys
# coding=UTF-8

# 删除变量
a, b, c = 1, True, "text"
del a, b

# 判断变量类型
print type(c)

# 输出第二个字符
print c[1]

# 输出第二个之后的字符
print c[1:]

# 连续输出两次
print c * 2

# List列表
list = ['abcd', 786, 2.23, 'runoob', 70.2]
print list[0:]

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
array = (1, True, "text")

# in表达式，意思：True是否在元组里
# not in 已 in 相反
if True in array:
    print 'True在元组里'

"""
多行注释
"""

# 2的3次幂
print 2 ** 3

# 取整除 - 返回商的整数部分
print 9 // 2

# 布尔 与
if True and True: print
# 布尔 或
if True or True: print
# 布尔 非
if not True: print

# is 判断 对象是否引用自某个类
# not is 与 is相反

# 字符串格式化
print "我叫 %s ,今年 %d 岁。" % ('徐会闯', 21)

# 字典是一种可变容器，可以存储各种类型的数据，是以键值对形式存储
lists = {'fda':'fas', 'ds':2}

# while 与 else配合
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
