import psycopg2
def fengzhuang(re_payload,token,m_type,chatId):
    return_json = {}
    return_json["chatId"] = str(chatId)
    return_json["token"] = str(token)
    return_json["messageType"] = int(0)
    return_json["payload"] = {'text':re_payload['text']}
    return return_json

import requests
def sendfengzhuang(reaction):
    url = 'https://ex-api.botorange.com/message/send'
    myobj =reaction


    x = requests.post(url, json = myobj)

    print(myobj)   
    return True

def change_q_process(contactId,new_q_process):
    # connect to the postgresql
    db_host_id = "127.0.0.1"
    db_name = "jhu_cssa"
    db_pass = "12345"
    db_owner = "postgres"
    db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    cursor = db_connection.cursor()
    # get data
    select_data = (
                """ UPDATE usres
                SET q_process = %s
                WHERE wechat_id = %s""" )
    # create the table
    cursor.execute(select_data,(str(new_q_process), str(contactId)))
    db_connection.commit()
    return True

def change_attr(contactId,change,change_value):
    # connect to the postgresql
    db_host_id = "127.0.0.1"
    db_name = "jhu_cssa"
    db_pass = "12345"
    db_owner = "postgres"
    db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    cursor = db_connection.cursor()
    # get data
    select_data = (
                """ UPDATE usres
                SET """+change+""" = %s
                WHERE wechat_id = %s""" )
    # create the table
    cursor.execute(select_data,(str(change_value), str(contactId)))
    db_connection.commit()
    return True

def find_attr(contactId,change):
    # connect to the postgresql
    db_host_id = "127.0.0.1"
    db_name = "jhu_cssa"
    db_pass = "12345"
    db_owner = "postgres"
    db_connection = psycopg2.connect(host=db_host_id,dbname=db_name, user=db_owner , password=db_pass)
    cursor = db_connection.cursor()
    # get data
    select_data = (
                """ select """+change+""" 
                from usres
                WHERE wechat_id = \'""" + contactId +"\'") 
    # create the table
    cursor.execute(select_data)
    records = cursor.fetchall()[0][0]
    return records

def fengzhuanglaqun(token,contact_id,group_id):
    return_json = {}
    return_json["token"] = str(token)
    return_json["botUserId"] = str("jhuJiaQunXiaoZhuShou")
    return_json["contactWxid"] = str(contact_id)
    return_json["roomWxid"] = str(group_id)
    return return_json

#?????????
col_group_id_dict = {
    "?????????":"R:10873310938958896",
    "????????????":"R:10797472880677411",
    "????????????":"R:10770814398210541",
    "?????????":"R:10722131315561425",
    "????????????":"R:10709262382973355",
    "??????????????????":"R:10867816937630185",
    "??????????????????":"R:10725601221764378",
    "?????????":"R:10725601221764378",
    "????????????":"R:10725601221764378",
    "??????":"R:10911976821439718",
    "??????":"R:10865826059558009"
}


def laqun(re_json):
    url = 'https://ex-api.botorange.com/room/addMember'
    myobj =re_json
    print("laqun??????",re_json)

    x = requests.post(url, json = re_json)
    print("???????????????",x.text)
    return True


