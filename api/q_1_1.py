import myutils

def func_q_1_1 (token,m_type,chatId,contactId,payload):
    #record info
    change = "a_bsphd"
    rec_dict = {"A":"本科生","B":"研究生","C":"博士生/访问学者","D":"已毕业"}
    year = rec_dict[payload]
    myutils.change_attr(contactId,change,change_value=year)

    #change q_process,通过contactId定位
    myutils.change_q_process(contactId,new_q_process="1_2")

    #define payload
    re_payload = {}
    re_mess = "您项目的所在城市为？\n\nA. 巴尔的摩\nB. 华盛顿DC\nC. 其他"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json