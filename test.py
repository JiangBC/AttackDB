import db
import json
import pprint
import data

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
    pprint.pprint(d)

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


def country_count():
    plan_dict={}
    country = list()
    num_sum = list()
    a = db.get_protocol_count("all")
    res = db.get_ip()
    for at_ip in res:
        at_info = db.get_ip_info(at_ip)
        country.append(at_info[0]["country"])
    country = list(set(country))
    for i in country:
        num_sum.append(0)
    for at_ip in res:
        num = db.get_ip_count(at_ip)
        at_info = db.get_ip_info(at_ip)
        x = country.index(at_info[0]["country"])
        num_sum[x] = num_sum[x]+num
    for i in range(len(country)):
        t = float(num_sum[i])*100/float(a)
        t = round(t,3)
        pct = str(t)+"%"
        plan_dict[country[i]] ={'num': num_sum[i], 'pct' : pct }
    return plan_dict

def country_count_nohttp():
    plan_dict={}
    country = list()
    num_sum = list()
    a = db.get_protocol_count("modbus")
    a = a + db.get_protocol_count("s7comm")
    a = a + db.get_protocol_count("bacnet")
    res = db.get_ip()
    for at_ip in res:
        at_info = db.get_ip_info(at_ip)
        country.append(at_info[0]["country"])
    country = list(set(country))
    for i in country:
        num_sum.append(0)
    for at_ip in res:
        num = 0
        num = db.get_ip_protocol_count(at_ip,"modbus")
        num = num + db.get_ip_protocol_count(at_ip,"s7comm")
        num = num + db.get_ip_protocol_count(at_ip,"bacnet")
        at_info = db.get_ip_info(at_ip)
        x = country.index(at_info[0]["country"])
        num_sum[x] = num_sum[x]+num
    for i in range(len(country)):
        t = float(num_sum[i])*100/float(a)
        t = round(t,3)
        pct = str(t)+"%"
        plan_dict[country[i]] ={'num': num_sum[i], 'pct' : pct }
    return plan_dict





def one_country_count():
    plan_dict={}
    res = db.get_ip()
    ip_con = list()
    ip_time = list()
    i = 0
    for at_ip in db.get_ip_from_country("CH"):
        if "bacnet" in db.get_ip_protocol(at_ip):
            data.attack_detailed_data(at_ip,num=200)

