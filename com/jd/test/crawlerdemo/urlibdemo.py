#coding=utf-8
import urllib
import urllib2

#get方式
# values={}
# values['username'] = "1016903103@qq.com"
# values['password']="XXXX"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?"+data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read()
#post方式
values={"keyfrom":"jdtest003","key":"1551773209","type:":"data","doctype":"json","version":"1.1","q":"dog"}
url="http://fanyi.youdao.com/openapi.do"
data=urllib.urlencode(values)
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)

print response.read()