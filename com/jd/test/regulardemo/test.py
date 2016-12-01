import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print 'ok'
else:
    print 'no'

print 'a b   c'.split(' ')
print re.split(r'\s+', 'a b     c')
print re.split(r'[\s\,\;]+', 'a,b, c  d;e')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
t='19:05:30'
m1 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m1.group(0),m1.group(),m1.group(1)
print re.match(r'^(\d+)(0*)$', '102300').groups()
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
re_email=re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')
print re_email.match('someone@gmail.com'),re_email.match('someone@gmail.com').group(0)