# -*- coding: utf-8 -*-

# import requests

# x = requests.get('https://ex-api.botorange.com/room/list?token=62c66439bacbe0a74279a6ff&current=0&pageSize=80')
# a = x.text
# f = open("txt_groupn_code.txt", "a")
# f.write(a)
# f.close()

import requests

url = 'https://ex-api.botorange.com/message/send'
myobj = {"chatId": "62e3fa962f47ac820ba925fa", 
"token": "62c66439bacbe0a74279a6ff", 
"messageType": 0, 
"payload": {"text": "您好，请问您所在学院？1.SAIS 2.AAP 3.Carey 4.Public Health 5.Whiting 6.Education 7.Peabody 8.School of Nursing 9.School of Medicine 10.其他"},
 "externalRequestId": "1"}

myobj ={
    "chatId": "62e3fa962f47ac820ba925fa",
    "token": "62c66439bacbe0a74279a6ff",
    "messageType": 0,
    "payload": {
        "text": "aaaa",
    }
    }

x = requests.post(url, json = myobj)

print(myobj)
