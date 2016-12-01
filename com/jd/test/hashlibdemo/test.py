import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

str1='d26a53750bc40b38b65a520292f69306'
if str1=='d26a53750bc40b38b65a520292f69306':
    print 'ok'