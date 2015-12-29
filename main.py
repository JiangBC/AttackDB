
import db
import pprint
import data


#res = list()
#res = db.get_ip()
#insert ip info to mongodb
#for res_i in res:
#	print res_i
#	if db.get_ip_info(res_i):
#		print 'pass'
#	else:
#		db.insert_ip_info(db.get_url_ip_info(res_i))
#		print 'insert'
#	i=i+1
#	print i
#	print '======================'


#get ip info from db
#pprint.pprint(db.get_db_attack_ip_info(res[0]))

#print "====================="
#x = '188.138.1.218'
##print x
#pprint.pprint(db.attack_ip_protocol(x))
#hh = db.attack_ip_protocol(x)
#for hh_i in hh:
#	print hh_i
#	print db.attack_ip_protocol_count(x,hh_i)
#print "====================="
#print db.get_attack_ip_count(x)

data.attack_detailed_data(at_ip='158.69.192.207',num=10)
#data.attack_detailed_data()