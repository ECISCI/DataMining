import sys
import os
import requests
import math

print("python encoding", sys.getdefaultencoding())

# 获取当前的编码格式
print("hello ", sys.getdefaultencoding())

# python编码
name = "程序员"
print(name.encode())
#
#
# 输出当前路径
print(os.getcwd())

g_text = requests.get("https://www.baidu.com")
print(g_text)
print(g_text.encoding)
print(g_text.url)

print(math.sin(90))

a = 0
print(type(a))
