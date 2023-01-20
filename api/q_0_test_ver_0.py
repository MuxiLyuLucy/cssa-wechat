import random
import myutils
import q_2_3_0
import mail

def func_q_0_test_ver_0 (token,m_type,chatId,contactId,payload):
    #寻找其认证信息
    change = "ver_torf"
    col_name = myutils.find_attr(contactId,change)
    payload = str(payload)
    if col_name != "t":
        #发邮件，需要邮箱，记录验证码在数据库
        r_data = str(random.randint(1000,9999))
        #record info
        change = "ver_id"
        myutils.change_attr(contactId,change,change_value=r_data)

        #record info
        change = "ver_mail"
        myutils.change_attr(contactId,change,change_value=payload)

        mail.send_e_main(r_data,payload)

        #change q_process,通过contactId定位
        myutils.change_q_process(contactId,new_q_process="ver_1")
               
        #define payload
        re_payload = {}

        re_mess = "我们已经发送验证邮件至您的JHU邮箱（可能在垃圾信箱），请您输入4位数验证码。若邮箱填写错误，请回复B重新开始。"

        re_payload["text"] = re_mess
        re_payload["mention"] = []

        #封装成json
        re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

        return re_json
    else:
        return q_2_3_0.func_q_2_3_0(token,m_type,chatId,contactId,"1")