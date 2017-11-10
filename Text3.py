# coding=UTF-8

# 创建文件，并写入文件
f = open("t.txt", "w")
f.write("写入t.txt")
f.close()

# 读取文件
f = open("t.txt", "r")
str = f.read()
print str

# python 异常处理
try:
    x = int(input("Please enter a number: "))
except (NameError, ValueError) as err:
    print("Oops!  That was no valid number.  Try again   ")

# 抛出异常 raise
raise NameError('HiThere')

class Text:
    publict = ''
    __ss__ = ""
    def text(self):

        return

