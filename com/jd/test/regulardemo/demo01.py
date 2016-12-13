#coding=utf-8
import re

str_code='xxIxxdjksjdskjxxlovexxadas899xxyouxxlo9d'
#.使用
# astr='xyz123'
# b=re.findall('x...',astr)
# print b
#*的使用
# astr='xyxy123'
# b=re.findall('x*',astr)
# print b
# #?使用
# astr='xy123'
# b=re.findall('x?',astr)
# print b
#.*使用
# b=re.findall('xx.*xx',str_code)
# print b
# b=re.findall('xx.*?xx',str_code)
# print b
# b=re.findall('xx(.*?)xx',str_code)
# print b
# ss='''xxIxxdjksjdskjxxlove
#    xxadas899xxyouxxlo9d'''
# b=re.findall('xx(.*?)xx',ss)
# print b
# ss='''xxIxxdjksjdskjxxlove
#    xxadas899xxyouxxlo9d'''
# b=re.findall('xx(.*?)xx',ss,re.S)
# print b
# sss='xxIxxdjksjdskjxxlove' \
#    'xxadas899xxyouxxlo9d'
# b=re.findall('xx(.*?)xx',sss,re.S)
# print b
#findall与search的区别
# astr='adxxIxx123xxlovexxdd2'
# f=re.search('xx(.*?)xx123xx(.*?)xx',astr).group(0)
# print f
# astr='adxxIxx123xxlovexxdd2'
# f=re.findall('xx(.*?)xx123xx(.*?)xx',astr)
# print f[0][0],f[0][1]
#sub的使用
# ss='123ddji32j123'
# b=re.sub('123(.*?)123','123%s123'%'GYQ',ss)
# print b
#不要使用compile
# sss='xxIxxdjksjdskjxxlovexxadas899xxyouxxlo9d'
# b=re.findall('xx(.*?)xx',sss,re.S)
# print b
# par='xx(.*?)xx'
# new_par=re.compile(par,re.S)
# b=re.findall(new_par,sss)
# print b
#匹配纯数字
astr='ad1kii89kl0lkk3232'
b=re.findall('(\d+)',astr)
alist=[]
strList=[]
for i in astr:
    if str.isdigit(i):
        alist.append(i)
    else:
        strList.append(i)
alist.sort()
print alist
strList.sort()
print strList

