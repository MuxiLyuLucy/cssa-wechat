# import requests

# x = requests.get('https://ex-api.botorange.com/room/list?token=62c66439bacbe0a74279a6ff&current=0&pageSize=80')
# a = x.text
# f = open("txt_groupn_code.txt", "a")
# f.write(a)
# f.close()

# import requests

# url = 'https://ex-api.botorange.com/message/send'
# myobj ={
#   "chatId": "62e3fa962f47ac820ba925fa",
#   "token": "62c66439bacbe0a74279a6ff",
#   "messageType": 0,
#   "payload": {
#     "text": "aaaa",
#   },
#   "externalRequestId": "1",
# }


# x = requests.post(url, json = myobj)

# print(myobj)


import requests

x = requests.get('https://ex-api.botorange.com/room/list?token=62c66439bacbe0a74279a6ff&current=0&pageSize=80')
a = x.text
f = open("txt_groupn_code.txt", "a")
f.write(a)
f.close()

print(a)