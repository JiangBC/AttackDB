import db
import json
import pprint

def protocol_shows():
    pro = ["http","modbus","s7comm","bacnet"]
    d = {}
    a = db.get_protocol_count("all")
    for pro_i in pro:
        pro_num = db.get_protocol_count(pro_i)
        t = float(pro_num)*100/float(a)
        t = round(t,2)
        pct = str(t)+"%"
        d[pro_i]={'num':pro_num, 'pct':pct}
    j_d = json.dumps(d)

def get_top_10_ip():
    ipd = {}
    res_ip = list()
    res_num = list()
    res_sort = list()
    top = [{"ip",0}]
    end = 0
    for at_ip in db.get_ip():
        num = db.get_ip_count(at_ip)
        res_ip.append(at_ip)
        res_num.append(num)
        res_sort.append(num)
    res_sort.sort(reverse=True)
    for i in range(10):
        end = res_num.index(res_sort[i])
        ipd[str(i+1)] = {res_ip[end]:res_sort[i]}
        res_num[end] = 0
    return ipd

ss = {}
ss = get_top_10_ip()
pprint.pprint(ss)