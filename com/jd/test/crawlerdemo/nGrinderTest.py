#coding=utf-8
import requests
import json
import re

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
cookies={cookieKey:cookieValue}
# print cookieKey,cookieValue
# for k,v in s.cookies.iteritems():
#     if k.startswith("JSESSIONID"):
#         print k+"="+v
# clone_and_start_url="http://192.168.172.43:8019/perftest/api/85/clone_and_start"
# rc=requests.get(clone_and_start_url,cookies=cookies)
# print rc.text
detail_report_url="http://192.168.172.43:8019/perftest/85/detail_report"
rd=requests.get(detail_report_url,cookies)
# print rd.text
pattern=re.compile('<th>(.*?)</th>.*?<td>(.*?)</td>',re.S)
tps_pan=re.compile('<strong>(.*?)</strong>')
test_time=re.compile('<span>(.*?)</span>')
items=re.findall(pattern,rd.text)
for item in items:
    if item[0]=='TPS':
        print item[1]
    elif item[0]=='Peak TPS':
        print item[1]
    elif item[0]=='Mean Test Time':
        print item[1]
    elif item[0]=='Executed Tests':
        print item[1]
    elif item[0]=='Successful Tests':
        print item[1]
    elif item[0]=='Errors':
        print item[1]
    else:
        pass