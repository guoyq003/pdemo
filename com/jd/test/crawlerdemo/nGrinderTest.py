#coding=utf-8
import requests
import json

loginURL="http://192.168.172.43:8019/form_login"
loginValue={"j_username":"admin","j_password":"admin","native_language":"cn","user_timezone":"Asia/Shanghai"}
#
# r=requests.post(loginURL,loginValue)
# print r.headers
#因为cookie的原因，尽量每次请求新建一个连接
s=requests.session()
s.post(loginURL,loginValue)
cookieKey=s.cookies.items()[0][0]
cookieValue=s.cookies.items()[0][1]
print cookieKey,cookieValue
# for k,v in s.cookies.iteritems():
#     if k.startswith("JSESSIONID"):
#         print k+"="+v
clone_and_start_url="http://192.168.172.43:8019/perftest/api/85/clone_and_start"
cookies={cookieKey:cookieValue}
r=requests.get(clone_and_start_url,cookies=cookies)
print r.text