import myutils

def func_q_2_1 (token,m_type,chatId,contactId,payload):

    #record info
    # change = "a_major"
    # rec_dict = {"A1":"A1","A2":"A2","A3":"A3","99":"99"
    #             ,"B1":"B1","B2":"B2","B3":"B3","B4":"B4","B5":"B5","B6":"B6","B7":"B7"
    #             ,"C1":"C1","C2":"C2","C3":"C3","C4":"C4"
    #             ,"D1":"D1","D2":"D2","D3":"D3","D4":"D4"
    #             ,"E1":"E1","E2":"E2","E3":"E3","E4":"E4","E5":"E5","E6":"E6","E7":"E7","E8":"E8","E9":"E9","E10":"E10","E11":"E11","E12":"E12","E13":"E13"
    #             ,"F1":"F1"}
    change = "a_colg"
    rec_dict = {"A":"工学院","B":"文理学院","C":"音乐学院","D":"商学院","E":"教育学院"
    ,"F":"国际关系学院","G":"公共卫生学院","H":"医学院","I":"护理学院"}
    year = rec_dict[payload]
    myutils.change_attr(contactId,change,change_value=year)

    #change q_process,通过contactId定位
    myutils.change_q_process(contactId,new_q_process="2_2")

    #define payload
    re_payload = {}

    #re_mess = "您好，请问您有什么需求？1.加入学院群 2.进入JHU微信小程序"
    re_mess = "恭喜您完成问答题部分，离加群只剩最后一步验证了。\n\n若继续验证，请回答“A”以继续。\n\n 注：若信息填写错误，请输入”B”重新开始。"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json