#coding=utf-8
import requests
import json

# r.status_code #响应状态码
# r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# #*特殊方法*#
# r.json() #Requests中内置的JSON解码器
# r.raise_for_status() #失败请求(非200响应)抛出异常
#SSL验证
# r = requests.get('https://www.baidu.com/', verify=False)
# print r.text
#URL后直接带参数
# url="http://fanyi.youdao.com/openapi.do?keyfrom=jdtest003&key=1551773209&type=data&doctype=json&version=1.1&q=dog"
# request=requests.get(url)
# print request.status_code
# print request.url
# print request.text
values={"keyfrom":"jdtest003","key":"1551773209","type":"data","doctype":"json","version":"1.1","q":"dog"}
url="http://fanyi.youdao.com/openapi.do"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36","Accept-Language":"zh-CN,zh;q=0.8"}
r=requests.post(url,values,headers=headers)
# print r.url
# print r.status_code
print (tuple(r.cookies))
print r.headers
# print r.content
# print r.encoding
print (r.text, '\n{}\n'.format('*'*79), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*'*79), r.encoding)

# url = 'http://httpbin.org/cookies'
# cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
# # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
# r = requests.get(url, cookies=cookies)
# print(r.json())

r1 = requests.get('https://api.github.com/user', auth=('guoyq003', 'dic2041'))
print r1.text
print r1.json()
