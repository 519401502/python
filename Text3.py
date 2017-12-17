# coding=UTF-8

# 创建文件，并写入文件
import urllib
#
# f = open("t.txt", "w")
# f.write("写入t.txt")
# f.close()
#
# # 读取文件
# f = open("t.txt", "r")
# str = f.read()
# print str
#
# # python 异常处理
# try:
#     x = int(input("Please enter a number: "))
# except (NameError, ValueError) as err:
#     print("Oops!  That was no valid number.  Try again   ")
#
# # 抛出异常 raise
# raise NameError('HiThere')
#
# class Text:
#     publict = ''
#     __ss__ = ""
#     def text(self):
#
#         return
#
#     def text2(self):
#         # 异常处理
#         try:
#             print ''
#         except:
#             print ''
#         return
#
#
#
# if __name__ == '__main__':
#     # or 表达式使用，以及 and
#     if True or True:
#         # 除完之后还是整数
#         # print 10 // 3
#         # hashmap = {'1': '1', '2': '2'}
#         # array = ['1', '2', '3']
#         # print array
#         # print hashmap
#         # print 'ok'
#         # abs 函数
#         print abs(-1)
# #         max函数
#         print max(1,2)
# #         min 函数
#         print min(2,3)
#     # 转换成字符串
#     str(1)
# #     转换成int
#     int('2')
# #     转换成bool
#     bool(
#
#     )
#     float()
from Tkinter import Image

from PIL import Image, ImageFilter

with Image.open('aaa.jpg') as image:
    w,h = image.size
    image.filter(ImageFilter.BLUR).save('aa.jpg', 'jpeg')



