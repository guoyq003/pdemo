#coding: utf-8
import itertools
#count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来
# natuals = itertools.count(1)
# for n in natuals:
#     print n
#cycle()会把传入的一个序列无限重复下去
# cs=itertools.cycle('abc')
# for c in cs:
#     print c
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns=itertools.repeat('a',10)
# count=0
# for n in ns:
#     print n,
#     count=count+1
# print count
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('abc','xzy'):
    print c,
print
#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('aaaabbccxxyzz'):
    print key,list(group)