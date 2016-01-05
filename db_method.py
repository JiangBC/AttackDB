import db
import sys
import pprint

def update_ipinfo():
    i = 1
    j='*'
    res = db.get_update_ip()
    l = len(res)
    k = l/50
# insert ip info to mongodb
    for res_i in res:
        sys.stdout.write("      "+str(int((i*100/l)))+'%  ||'+j+'->'+"\r")
        if i >= k:
            j += '*'
            k = k+l/50
        i=i+1
        if db.get_ip_info(res_i):
            sys.stdout.write(" Pass "+"\r")
        else:
            sys.stdout.write("insert"+"\r")
            db.insert_ip_info(db.get_url_ip_info(res_i))
    print "Ipinfo Update OK"


def attack_detailed_shows(at_ip='8.8.8.8', num=2):
    i = 0
    k = 1
    if db.get_ip_count(at_ip)==-1:
        print "can't find this ip!"
        return
    print "all attack count : %d"%(db.get_ip_count(at_ip))
    for at_pro in db.get_ip_protocol(at_ip):
        print "%s : %d"%(at_pro,db.get_ip_protocol_count(at_ip, at_pro))
    session_id = db.get_session_id(at_ip)
    for s_id in session_id:
        hpfeed_data = db.transform_session_to_hpfeed(s_id)
        session_data = db.get_session_data(s_id)
        info_dict = {"source_ip":at_ip,
                 "source_port":session_data["source_port"],
                 "destination_port":session_data["destination_port"],
                 "protocol":(session_data["protocol"]).encode("utf-8"),
                 "timestamp":session_data["timestamp"],
                 "data":hpfeed_data["payload"]["data"]}
        if hpfeed_data["payload"]["public_ip"]:
            info_dict['public_ip'] = (hpfeed_data["payload"]["public_ip"]).encode("utf-8")
        else:
            info_dict['public_ip'] = hpfeed_data["payload"]["public_ip"]
        print "The %d :"%(k)
        k = k + 1
        pprint.pprint(info_dict)
        i = i + 1
        if i == num:
            print "========== Press Enter continue =========="
            if raw_input("Your choose:"):
                print "enough"
                break
            else:
                print "========== more 5 data =========="
                i = 0
    print "============end============="