# 加入学院群的提问
import myutils

def q_1_5(token,m_type,chatId,contactId):

    re_payload = {}
    re_mess = "您好。请问您是否要加入学院群？1: 是 2: 否"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json


def q_1_5_yes(token,m_type,chatId,contactId):

    re_payload = {}

def q_1_5_no(token,m_type,chatId,contactId):
    
    re_payload = {}
    re_mess = "谢谢！祝您生活愉快！"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json


def q_1_5_unclear(token,m_type,chatId,contactId):

    re_payload = {}
    re_mess = "请您回答1（是）或者2（否）"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json
