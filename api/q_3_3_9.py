import myutils

def func_q_3_3_9 (token,m_type,chatId,contactId,payload):
    #寻找其认证信息
    change = "ver_torf"
    col_name = myutils.find_attr(contactId,change)
    if col_name != "t":

        #change q_process,通过contactId定位
        myutils.change_q_process(contactId,new_q_process="ver_0")
               
        #define payload
        re_payload = {}

        re_mess = "您好，请输入您的jhu邮箱，我们将发送5位数验证码（有可能在垃圾箱，请查收）。"

        re_payload["text"] = re_mess
        re_payload["mention"] = []

        #封装成json
        re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

        return re_json
    
    if payload == "1":  #研究生群
        #change q_process,通过contactId定位
        myutils.change_q_process(contactId,new_q_process="3_3_9")

        #寻找其学院
        change = "a_colg"
        col_name = myutils.find_attr(contactId,change)

        #加群
        col_group_id_dict = myutils.col_group_id_dict
        group_id = col_group_id_dict[col_name]

        #封装成json
        re_json = myutils.fengzhuanglaqun(token,contactId,group_id)
        #拉群
        myutils.laqun(re_json)

        # record
        change = "b_group"
        myutils.change_attr(contactId,change,change_value=group_id)

        return re_json

    if payload == "2": #本科群
        #change q_process,通过contactId定位
        myutils.change_q_process(contactId,new_q_process="3_3_9")

        #加群
        group_id = "本科群号码"

        #封装成json
        re_json = myutils.fengzhuanglaqun(token,contactId,group_id)
        #拉群
        myutils.laqun(re_json)

        # record
        change = "b_group"
        myutils.change_attr(contactId,change,change_value=group_id)
        
        return re_json