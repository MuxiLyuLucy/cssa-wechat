import myutils

def func_q_1_2 (token,m_type,chatId,contactId,payload):

    #record info
    change = "a_baldc"
    rec_dict = {"A":"巴尔的摩","B":"华盛顿DC","C":"其他"}
    year = rec_dict[payload]
    myutils.change_attr(contactId,change,change_value=year)

    #change q_process,通过contactId定位
    myutils.change_q_process(contactId,new_q_process="2_1")

    #define payload
    re_payload = {}
    re_mess = "您目前所在的学院为？\n\nA. 工学院\nB. 文理学院\nC. 音乐学院\nD. 商学院\nE. 教育学院\nF. 国际关系学院\nG. 公共卫生学院\nH. 医学院\nI. 护理学院"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json