import json
try:
    import cPickle as pickle
except ImportError:
    import pickle
d=dict(name='tom',age=21,score=90)
pickle.dumps(d)
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
fr = open('dump.txt', 'rb')
dr = pickle.load(fr)
fr.close()
print dr

dd=dict(name='bob',age=22,score=93)
json_sr=json.dumps(dd)
print json_sr
json_str_new=json.loads(json_sr)
print json_str_new


