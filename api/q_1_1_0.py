import myutils

def func_q_1_1_0(token,m_type,chatId,contactId,payload):

    #record info
    change = "a_year"
    rec_dict = {"A":"2022","B":"2021","C":"2020","D":"2019","F":"其他"}
    year = rec_dict[payload]
    myutils.change_attr(contactId,change,change_value=year)

    #change q_process,通过contactId定位
    myutils.change_q_process(contactId,new_q_process="1_1")

    #define payload
    re_payload = {}
    re_mess = "您目前在读的学位是？\n\nA. 本科生\nB. 研究生\nC. 博士生/访问学者\nD. 已毕业"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json