#coding=utf-8
import os
#当前目录
print os.path.abspath('.')
#路径合并
#也不要直接去拆字符串，而要通过os.path.split()函数，
#这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print os.path.join('gyq','test')
print os.path.split('D:\IdeaProjects\pydemo\com\jd\\test\\filedemo\demo.py')
#取得文件拓展名
print os.path.splitext('D:\IdeaProjects\pydemo\com\jd\\test\\filedemo\demo.py')
#创建删除目录
# os.mkdir('test')
# os.rmdir('test')
#文件重命名
# os.rename('gyq.txt','ptest.txt')
#删除文件
# os.remove('ptest.txt')
#列出当前目录下所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
for x in os.listdir('D:\IdeaProjects\pydemo\com\jd\\test\\filedemo'):
    if os.path.isfile(x):
        print x
#列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
