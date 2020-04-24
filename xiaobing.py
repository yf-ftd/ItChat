# coding = utf8
import requests
import time


def xiaobing(msg):
    uid = '5175429989'
    source = '209678993'
    SUB = '_2A25zpVgdDeRhGeRO6VIX9y7FwjmIHXVQ087VrDV8PUNbmtANLVHgkW9NUJEp5YIg84_GTvGQaCWNuZFdxf48os0V'
    url_send = 'https://api.weibo.com/webim/2/direct_messages/new.json'
    data = {'text': msg, 'uid': uid, 'source': source}
    headers = {'cookie': 'SUB=' + SUB, 'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/79.0.3945.130 Safari/537.36',
               'Referer': 'https://api.weibo.com/chat/'}
    response = requests.post(url_send, data=data, headers=headers).json()
    print(response)
    sendMsg = response['text']
    time.sleep(1)
    while True:
        url_get = 'https://api.weibo.com/webim/2/direct_messages/conversation.json?uid={}&source={}'.format(uid, source)
        response = requests.get(url_get, headers=headers).json()
        getMsg = response['direct_messages'][0]['text']
        if sendMsg == getMsg:
            time.sleep(1)
        else:
            return getMsg


weatherInfo = xiaobing("北京天气")
print(weatherInfo)
