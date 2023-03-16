# Date: 2019/02/16   
# 这是一个练习python的文档
# python 版本3.7.2           
# 编辑器  vs code 
 

#coding:utf-8  编码格式
# python 之禅
import this 


import sys

'''
title() 以首字母大写的方式显示每个单词
lower()  小写    
upper()  大写
rstrip()  删除末尾空白
lstrip()  删除行首空白
strip()  删除空白
print在python2 中是不需要括号的.
3*0.1 =0.300000000000004
str()  转换成字符串输出
'''


messgae = " Albert Einstein said, \"A peroson who nerver made a mistake never tried anything new.\" "
print(messgae.title().lower())  


list =['a','b','c','d','E','a']   #pyhon 用 [] 表示列表,并且用逗号分隔其中的元素.
print(list[-1].title())   
list[0]=''   
list.append('amos')  # 末尾添加元素
list.insert(2,'') # 指定位置插入元素


# 删除之后不再使用,就用del   
# 删除之后,继续使用则用pop
# 根据值删除元素, remove().且此方法只删除第一个值.
del list[-1]   #根据索引删除元素


#首字母顺序排序 且永远更改位置. reverse=True为倒序
list.sort(reverse=True)
print(list)


name ='請告訴我你的名字：'
a=''
while a !='' :
      a =input('请告訴我你的名字：')
      print('欢迎您，'+a)
      print("您不是root用戶，所以即将退出！")
