# coding=UTF-8

# 为线程定义一个函数
import time

import thread


def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 开启一个线程
thread.start_new_thread(print_time, ("Thread-1", 2, ) )
