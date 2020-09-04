# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:bw_2004
# File_name:dingding.py.py
# Author: lt
# Time:2020年09月04日
import json
import requests

class Ding():
    def message(link=1):
        url = 'https://oapi.dingtalk.com/robot/send?access_token=6e2e35a5591b4bd70a1249ca938e0d99355ceb4a63929c61fc2711792fb28424'
        pagrem = {
            "msgtype": "text",
            "text": {
                "content": "：%s " % ('你好坏哦~')
            },
            "at": {
                "atMobiles": [
                    "17691125909"  # 需要填写自己的手机号，钉钉通过手机号@对应人
                ],
                "isAtAll": True # 是否@所有人，默认否
            }
        }
        headers = {
            'Content-Type': 'application/json'
        }
        requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    Ding.message()
