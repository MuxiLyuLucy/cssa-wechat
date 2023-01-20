
import myutils

def func_q_2_3_0 (token,m_type,chatId,contactId,payload):
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
        
        #define payload
        re_payload = {}

        if unpos_name == "本科生":

                re_mess = "您好，同学您好，以下为您目前可以加入的群聊，请回复字母以选择：\n\n A. JHU Current Undergrads 2022 \n\n B. " + str(col_name) + str("群")

        elif unpos_name == "研究生":

                re_mess = "您好，同学您好，以下为您目前可以加入的群聊，请回复字母以选择：\n\n B. " + str(col_name) + str("群")

        elif unpos_name == "博士生/访问学者":

                re_mess = "您好，同学您好，以下为您目前可以加入的群聊，请回复字母以选择：\n\n A. JHU PhD群 2022 \n\n B. " + str(col_name) + str("群")

        else:
                re_mess = "我们正在逐步开放功能，过来会有更多适合您的的群聊。"

        re_payload["text"] = re_mess
        re_payload["mention"] = []

        #封装成json
        re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

        return re_json          
