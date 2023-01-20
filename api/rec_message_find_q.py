import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import test_and_add_user
import rec_message_proce_q
import myutils

def find_q(dict_data):
    contactId = dict_data["contactId"]
    payload = dict_data["payload"]
    chatId = dict_data["chatId"]
    m_type = dict_data["m_type"]
    # find the question's position
    q_in_sql = find_q_in_sql(contactId)
    # react to the payload
    print("所处问题",q_in_sql)
    reaction = rec_message_proce_q.process_q(q_in_sql,m_type,contactId,payload,chatId)
    print(reaction)
    myutils.sendfengzhuang(reaction)
    return None

def find_q_in_sql(contactId):
    input_wechat_id = contactId
    q_in_sql = test_and_add_user.test_add_user(input_wechat_id,req_tag="req_find_q")
    return q_in_sql


