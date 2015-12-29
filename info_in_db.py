import db
import pprint
import pymongo
import urllib2
import json


client = pymongo.MongoClient('192.168.3.115', 27017)
at = client.mnemosyne

res = list()
res_list = list()
test_1 = list()
res = db.get_ip()
res_list=db.get_session_id(res[1])

# it = list(db.get_test(res[0]))
pprint.pprint(res_list)
print db.get_ip_count(res[1])
#print res_dict
print '================test_1======================='
for item in at.session.find({"_id":res_list[0]}):
	test_1.append(item["hpfeed_id"])
	print item

print test_1
print '================test_hpfeed======================='
ss=list(at.hpfeed.find({"_id":test_1[0]}))
pprint.pprint(ss)