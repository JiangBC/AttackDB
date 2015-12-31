import pymongo
import urllib2
import json


client = pymongo.MongoClient('192.168.3.115', 27017)
db = client.mnemosyne


def get_session_id(at_ip):
    id_list = list()
    for item in db.session.find({"source_ip":at_ip}).sort("timestamp"):
        id_list.append(item["_id"])
    return id_list


def get_session_data(session_id):                                              
    return db.session.find_one({"_id":session_id})


def transform_session_to_hpfeed(session_id):
    item = db.session.find_one({"_id":session_id})
    hpfeed_id = item["hpfeed_id"]
    return db.hpfeed.find_one({"_id":hpfeed_id})


def get_update_ip():
    ip_list = list()
    for item in db.session.find():
        ip_list.append((item["source_ip"]).encode("utf-8"))
    ip_list = list(set(ip_list))
    return ip_list
# type = list


# ip from ipinfo
def get_ip():
    ip_list = list()
    for item in db.ipinfo.find():
        ip_list.append((item["ip"]).encode("utf-8"))
    return ip_list


# need to better
def get_ip_count(at_ip):
    exist_ip = list(db.session.find(
                    {"source_ip": at_ip},
                    {"source_ip": 1, "_id": 0}))
    if exist_ip:
        sum_num = db.session.find({"source_ip": at_ip}).count()
        return sum_num
    else:
        return -1
# type = int


def get_url_ip_info(at_ip):
    url = "http://ipinfo.io/"+at_ip+"/json"
    ipinfo = urllib2.urlopen(url)
    dict_ipinfo = json.load(ipinfo)
    return dict_ipinfo
# type = dict


def insert_ip_info(need_insert_info):
    db.ipinfo.insert(need_insert_info)


def get_ip_info(at_ip):
    dbipinfo = list(db.ipinfo.find({"ip": at_ip}, {"_id": 0}))
    return dbipinfo
# type = list


def get_ip_protocol(at_ip):
    protocol_list = list()
    for item in db.session.find({"source_ip": at_ip}):
        protocol_list.append((item["protocol"]).encode("utf-8"))
    protocol_list = list(set(protocol_list))
    return protocol_list


def get_ip_protocol_count(at_ip, protocol):
    sum_num = db.session.find(
              {"source_ip": at_ip, "protocol": protocol}).count()
    return sum_num


def get_protocol_count(protocol):
    if "all" in protocol:
        return db.session.find().count()
    else:
        return db.session.find({"protocol": protocol}).count()

def get_test(at_ip):
    return db.session.find({"source_ip": at_ip})