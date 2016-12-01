import codecs
with codecs.open('gyq.txt','w','UTF8') as f:
    f.write('you are dog!\n please input fuck!')
with codecs.open('gyq.txt','r','gbk') as f:
    for line in f.readlines():
        print line.strip()
