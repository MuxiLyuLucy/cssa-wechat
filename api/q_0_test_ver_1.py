import myutils
import q_2_3_0
import q_3_3_9
import q_2_2


def func_q_0_test_ver_1 (token,m_type,chatId,contactId,payload):
    #寻找其认证信息
    change = "ver_torf"
    col_name = myutils.find_attr(contactId,change)
    payload = str(payload)
    if payload == "B":
        return q_2_2.func_q_2_2(token,m_type,chatId,contactId,"A")

    if col_name != "t":
        
        #验证验证码

        #寻找其验证码
        change = "ver_id"
        col_name = myutils.find_attr(contactId,change)

        if str(col_name) != str(payload):
            return q_2_2.func_q_2_2(token,m_type,chatId,contactId,"A")

        #record info
        change = "ver_torf"
        myutils.change_attr(contactId,change,change_value="t")

        return q_2_3_0.func_q_2_3_0(token,m_type,chatId,contactId,"1")
    else:
        return q_2_3_0.func_q_2_3_0(token,m_type,chatId,contactId,"1")