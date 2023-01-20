# import myutils

# def func_q_1_3 (token,m_type,chatId,contactId,payload):

#     #record info
    # change = "a_colg"
    # rec_dict = {"1":"SAIS","2":"AAP","3":"Carey","4":"Public Health","5":"Whiting"
    # ,"6":"Education","7":"Peabody","8":"School of Nursing","9":"School of Medicine","10":"其他"}
    # year = rec_dict[payload]
#     myutils.change_attr(contactId,change,change_value=year)

#     #change q_process,通过contactId定位
#     myutils.change_q_process(contactId,new_q_process="2_1")

#     #define payload
#     re_payload = {}
#     tongyi = "您好，请问您的专业(未找寻到选项则选'其他')？"

#     if payload == "1":
#         re_mess = tongyi + "A1.MAIA A2.MIEF A3.MAIR 99.其他"
#     if payload == "2":
#         re_mess = tongyi + "B1.Applied Economics B2.Bioinformatics B3.Biotechnology B4.Communication B5.Film and Media B6.Government B7.Public Management 99.其他"
#     if payload == "3":
#         re_mess = tongyi + "C1.Information System C2.Finance C3.Marketing C4.MBA 99.其他"
#     if payload == "4":
#         re_mess = tongyi + "D1.MPH D2.MHS D3.ScM D4.PhD/DrPH 99.其他"
#     if payload == "5":
#         re_mess = tongyi + "E1.Artificial Intelligence E2.Biomedical Engineering E3.Chemical and Biomolecular Engineering E4.Civil Engineering E5.Computer Science E6.Data Science E7.Electrical and Computer Engineering E8.Engineering Management E9.Environmental Engineering E10.Financial Mathematics E11.Material Science and Engineering E12.Mechanical Engineering E13.System Engineering 99.其他"
#     if payload == "6":
#         re_mess = tongyi + "F1.ITGL 99.其他"
#     if payload == "7":
#         re_mess = tongyi + "99.其他"
#     if payload == "8":
#         re_mess = tongyi + "99.其他"
#     if payload == "9":
#         re_mess = tongyi + "99.其他"
#     if payload == "10":
#         re_mess = tongyi + "99.其他"



#     re_payload["text"] = re_mess
#     re_payload["mention"] = []

#     #封装成json
#     re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

#     return re_json