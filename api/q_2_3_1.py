import myutils

def func_q_2_3_1 (token,m_type,chatId,contactId,payload):
    #change q_process,通过contactId定位
    myutils.change_q_process(contactId,new_q_process="2_3_1")

    #寻找其本科 还是硕士 参考
        #rec_dict = {"A":"本科生","B":"研究生","C":"博士生/访问学者","D":"已毕业"}
    #寻找其本科 还是硕士
    change = "a_bsphd"
    unpos_name = myutils.find_attr(contactId,change)

    #寻找其学院 参考
        #rec_dict = {"A":"工学院","B":"文理学院","C":"音乐学院","D":"商学院","E":"教育学院"
        #            ,"F":"国际关系学院","G":"公共卫生学院","H":"医学院","I":"护理学院"}
    #寻找其学院
    change = "a_colg"
    col_name = myutils.find_attr(contactId,change)  

    # 学院群
    if payload == "B":
        #加群
        col_group_id_dict = myutils.col_group_id_dict
        group_id = col_group_id_dict[col_name]
        # record
        change = "b_group1"
        myutils.change_attr(contactId,change,change_value=group_id)

    elif unpos_name == "本科生" and payload == "A":
        #加群
        col_group_id_dict = myutils.col_group_id_dict
        group_id = col_group_id_dict["本科"]
        print("查本科的***："+str(group_id))
        # record
        change = "b_group2"
        myutils.change_attr(contactId,change,change_value=group_id)

    elif unpos_name == "博士生/访问学者" and payload == "A":
        #加群
        col_group_id_dict = myutils.col_group_id_dict
        group_id = col_group_id_dict["博士"]
        # record
        change = "b_group2"
        myutils.change_attr(contactId,change,change_value=group_id)

    else:
        re_payload = {}
        re_mess = "您的输入有误，请重新输入。"
        re_payload["text"] = re_mess
        re_payload["mention"] = []
        #封装成json
        re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)
        return re_json          

    #封装成json
    re_json = myutils.fengzhuanglaqun(token,contactId,group_id)
    #拉群
    myutils.laqun(re_json)
    
    #再加入新群
    re_payload = {}
    re_mess = "已将您拉入群，您可以继续回复大写字母来加入其他群。"
    re_payload["text"] = re_mess
    re_payload["mention"] = []
    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json
