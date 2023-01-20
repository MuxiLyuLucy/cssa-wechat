#!/usr/bin/python3
# encoding:utf-8
import flask
import json
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
app = flask.Flask(__name__) 
 
# 'index'是接口路径，methods不写，默认get请求     
@app.route('/index',methods=['get']) 
# get方式访问
def index():
  ren = {'msg':'成功访问首页','msg_code':200}
  #json.dumps 序列化时对中文默认使用的ascii编码.想输出中文需要指定ensure_ascii=False
  return json.dumps(ren,ensure_ascii=False)
 
 
#post入参访问方式二：josn格式参数  
@app.route('/message',methods=['post'])
def message():
  json_data = flask.request.json

  #检测是否群消息
  if len(json_data.get('data')['roomTopic']) != 0:
    return json.dumps({'msg':'群消息','msg_code':200},ensure_ascii=False)


  import rec_message_prase
  try:
    dict_message_use_info = rec_message_prase.analyze_rec_message(json_data)
  except:
    return json.dumps({'msg':'消息无法分析','msg_code':200},ensure_ascii=False)

  #拉群
  import rec_message_find_q
  rec_message_find_q.find_q(dict_message_use_info)
  print(dict_message_use_info)


  return json.dumps({'msg':'接收到消息','msg_code':200},ensure_ascii=False)
 
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
