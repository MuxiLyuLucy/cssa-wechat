
import q_0_0_notA
import q_0_0_isA
import q_1_1_0
import q_1_1
import q_1_2
import q_1_3
import q_2_1
import q_2_2
import q_2_3_1
import q_3_3_9
import q_2_3_0
import q_0_test_ver_0
import q_0_test_ver_1

def process_q(q_in_sql,m_type,contactId,payload,chatId):
    payload = str(payload)
    token =  "62c66439bacbe0a74279a6ff"
    # mail ver
    payload_tail = "edu" in payload

    if q_in_sql == "0_0" and payload != "A":
        #返回欢迎语
        print("这里是0_0_不是A")
        print(payload)
        re_mess_json = q_0_0_notA.welcome_0_0 (token,m_type,chatId,contactId)

    elif q_in_sql == "0_0" and payload == "A":
        #更改状态为1_1,并返回询问入学年份
        print("这里是0_0_A")
        re_mess_json = q_0_0_isA.welcome_0_0_isA(token,m_type,chatId,contactId)
    
    elif q_in_sql == "1_1_0" and payload in ["A","B","C","D","F"]:
        #记录入学年份/记录本科生
        re_mess_json = q_1_1_0.func_q_1_1_0(token,m_type,chatId,contactId,payload)


    elif q_in_sql == "1_1" and payload in ["A","B","C","D"]:
        #记录入学年份，更改状态为1_2,并返回询问校区
        re_mess_json = q_1_1.func_q_1_1(token,m_type,chatId,contactId,payload)


    elif q_in_sql == "1_2" and payload in ["A","B","C"]:

        #记录校区，更改状态为1_3,并返回询问学院
        re_mess_json = q_1_2.func_q_1_2(token,m_type,chatId,contactId,payload)

    elif q_in_sql == "2_1" and payload in ["A","B","C","D","E","F","G","H","I"]:

        #记录学院，更改状态为2_1,并返回询问确认与否
        re_mess_json = q_2_1.func_q_2_1(token,m_type,chatId,contactId,payload)

    # elif q_in_sql == "2_1" and payload in ['A1', 'A2', 'A3', '99', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'F1']:

    #     #记录专业，更改状态为2_2,并返回询问需求
    #     re_mess_json = q_2_1.func_q_2_1(token,m_type,chatId,contactId,payload)

    elif q_in_sql == "2_2" and payload in ['A','B']:

        #记录确定，更改状态为2_3,(若重新填写返回0_0) 2_3返回加群需求
        re_mess_json = q_2_2.func_q_2_2(token,m_type,chatId,contactId,payload)

    # elif q_in_sql == "2_3_0" and payload in ['A','B']:

    #     #加群，验证完后自动运行
    #     re_mess_json = q_2_3_0.func_q_2_3_0(token,m_type,chatId,contactId,payload)
        
    elif q_in_sql == "2_3_1": #and payload in ['A','B']:

        #加群
        re_mess_json = q_2_3_1.func_q_2_3_1(token,m_type,chatId,contactId,payload)

    # elif q_in_sql == "2_3" and payload in ['1','2']:

    #     #记录确定，更改状态为3_3_0
    #     re_mess_json = q_2_3_1.func_q_2_3_1(token,m_type,chatId,contactId,payload)


    # elif q_in_sql == "3_3_9" and payload in ['1','2']:

    #     #记录确定，更改状态为ver_0
    #     re_mess_json = q_3_3_9.func_q_3_3_9(token,m_type,chatId,contactId,payload)

    elif q_in_sql == "ver_0" and payload_tail:

        #记录确定，更改状态为ver_1
        re_mess_json = q_0_test_ver_0.func_q_0_test_ver_0(token,m_type,chatId,contactId,payload)

    elif q_in_sql == "ver_1" and (len(payload) == 4 or payload == "B") :

        #记录确定，更改状态为ver_1
        re_mess_json = q_0_test_ver_1.func_q_0_test_ver_1(token,m_type,chatId,contactId,payload)

    else:
        re_mess_json = 3

    print(re_mess_json)
    return re_mess_json
