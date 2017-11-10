# coding=UTF-8

# 创建文件，并写入文件
f = open("t.txt", "w")
f.write("写入t.txt")
f.close()

# 读取文件
f = open("t.txt", "r")
str = f.read()
print str