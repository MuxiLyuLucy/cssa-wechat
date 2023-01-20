import myutils

def welcome_0_0_isA (token,m_type,chatId,contactId):
    #change q_process,通过contactId定位
    myutils.change_q_process(contactId,new_q_process="1_1_0")


    #define payload
    re_payload = {}
    re_mess = "您的入学年份为？\n\nA. 2022\nB. 2021\nC. 2020\nD. 2019\nF. 其他" 
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json