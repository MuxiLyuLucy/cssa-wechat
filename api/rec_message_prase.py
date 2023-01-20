import json

def analyze_rec_message(json_data):
    dict_message_use_info = {}
    dict_message_use_info["chatId"] = json_data.get('data')['chatId']
    dict_message_use_info["contactName"] = json_data.get('data')['contactName']
    dict_message_use_info["contactId"] = json_data.get('data')['contactId']
    dict_message_use_info["payload"] = json_data.get('data')['payload']['text']
    dict_message_use_info["m_type"] = json_data.get('data')['type']

    return dict_message_use_info
