
import db
import pprint
import db_method


db_method.update_ipinfo()

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

# data.attack_detailed_data(at_ip='158.69.192.207',num=10)
#data.attack_detailed_data()