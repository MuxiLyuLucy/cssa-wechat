import myutils

def welcome_0_0 (token,m_type,chatId,contactId):
    #define payload
    re_payload = {}
    re_mess = "Hihi，同学你好呀! 我是JHU学联加群小助手，很高兴为您服务。\n\n目前小助手为初始阶段，学联为大家准备了学院群。若大范围加群未出现问题，过段时间学联将继续把兴趣群以及其他更多群聊加入小助手。若遇到问题，请添加学联小助手微信（wx：johnshopkinscssa）\n\n接下来我会以问答题的形式，确认您的学生身份以及大体信息，以便加您进入最正确的微信群聊。您只用回答大写字母A,B,C,D即可。\n\n如果您准备好了，回答“A”以继续"
    re_payload["text"] = re_mess
    re_payload["mention"] = []

    #封装成json
    re_json = myutils.fengzhuang(re_payload,token,m_type,chatId)

    return re_json
