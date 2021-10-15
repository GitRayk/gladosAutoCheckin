'''
Glados自动签到程序

checkin: post
https://glados.network/api/user/checkin
status: get
https://glados.network/api/user/status
'''

import requests

def getStrValue(resText, key):
    # 该函数以网页源码为参数，将键值对中的指定值返回
    resText = resText[1: -1]    # 去掉头尾的大括号
    resText = resText.replace('"', '')
    resText = resText.split(",")
    resText = map(lambda text: text.split(":"), resText)
    for TextList in resText:
        if key == TextList[0]:
            return TextList[1]
    return False

checkinUrl = "https://glados.network/api/user/checkin"
statusUrl = "https://glados.network/api/user/status"
cookie = "_ga=GA1.2.1368007815.1621871003; koa:sess=eyJjb2RlIjoiVkUwUjEtMkdQQzgtRlQ0MUwtR0JUQTgiLCJ1c2VySWQiOjgxODU2LCJfZXhwaXJlIjoxNjQ3NzkxMDMzNzEzLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=PdCamWWhCwliK8M24rAg5wPRsCs; _gid=GA1.2.2119754023.1634187949"
headers = {
    "cookie": cookie,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

data = {
    "token": "glados_network"
}

res = requests.post(checkinUrl, headers=headers, data=data)
# status = requests.get(statusUrl, headers=headers)

# 将自动签到结果通过server酱发送到微信
sendKey = "SCT85032TdGbBbPJpGaNuUXKjlL8JIgF2"
requests.post("https://sctapi.ftqq.com/" + sendKey + ".send?title=Glados签到结果&desp=" + getStrValue(res.text, "message") + ". 账户剩余天数为" + getStrValue(res.text, "balance").split(".")[0] + "天")
