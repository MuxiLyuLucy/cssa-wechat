import myutils
import q_0_0_notA

def func_q_2_2 (token,m_type,chatId,contactId,payload):


    if payload == "A":
        #change q_process,通过contactId定位
        myutils.change_q_process(contactId,new_q_process="ver_0")
        re_mess = "您好！恭喜您完成问答题部分，离加群只剩最后一步验证了！为了确保屏幕前的您是JHU的在校学生或毕业生，请输入您的JHU邮箱全称（后缀可是@jh.edu，@jhu.edu, 或@jhmi.edu）"
        #define payload
        re_payload = {}
        re_payload["text"] = re_mess
        re_payload["mention"] = []
        #封装成json
        re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

        return re_json

    if payload == "B":
        myutils.change_q_process(contactId,new_q_process="0_0")
        return q_0_0_notA.welcome_0_0(token,m_type,chatId,contactId)
