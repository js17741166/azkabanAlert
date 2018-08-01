# -*- coding: utf-8 -*-
# https://oapi.dingtalk.com/robot/send?access_token=18200f97032b410de1945348c80dcadad6b1a6d34ed3a1563d868b6abcba3472/
# !/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
# import sys
# import os
from db import mysql
from dateUtil import *

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=XXXXXX"


def msg(text):
    json_text = {
        "msgtype": "text",
        "at": {
            "atMobiles": [
                "18518407328"
            ],
            "isAtAll": True
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url, json.dumps(json_text), headers=headers).content


def getAzkabanSessionId():
    json_parms = {
        "action": "login",
        "username": "azkaban",
        "password": "bigdata@2018"
    }
    # azkaban_url= "https://172.17.10.14:8443"
    azkaban_url = "https://10.0.11.45:8445?action=login&username=azkaban&password=bigdata@2018"
    # print(requests.get(azkaban_url))
    req = requests.post(azkaban_url, headers=headers, verify=False).content
    req_json = json.loads(req)
    if req_json.has_key("status"):
        return req_json["session.id"]
    else:
        return ""


def get188AzkabanAlert(endTime):
    sql = """
           select *  from execution_flows
            where (flow_data like '%FAILED%' or  flow_data like '%KILLED%')
            and end_time>={}
                """.format(endTime)
    db = mysql("azkaban14")
    columns = db.query(sql).fetchall()
    return columns

def get29AzkabanAlert(endTime):
    sql = """
           select *  from execution_flows
            where (flow_data like '%FAILED%' or  flow_data like '%KILLED%')
            and end_time>={}
                """.format(endTime)
    db = mysql("azkaban29")
    columns = db.query(sql).fetchall()
    return columns


if __name__ == '__main__':
    currentDate = getCurrentDateTime()
    lastMinutes = dateAddInMinutes(currentDate, -1)
    lastTimastamp = getTimestamp(lastMinutes, False)
    print(lastMinutes)
    print(lastTimastamp)

    for c in get188AzkabanAlert(lastTimastamp):
        message = json.loads(c[11])
        try:
            updateTime = message["updateTime"]
            updateTimes = datetime.datetime.fromtimestamp(long(updateTime)/1000)
            projectName = message["projectName"]
            flowId = message["flowId"]
            status = message["status"]
            proxyUsers = message["proxyUsers"]
            text = """10.14 azkaban报警： {} {} at {} is {}""".format(projectName, flowId, updateTimes, status)
            msg(text)
        except:
            print("10.14 no alert")
    for c in get29AzkabanAlert(lastTimastamp):
        message = json.loads(c[11])
        try:
            updateTime = message["updateTime"]
            projectName = message["projectName"]
            flowId = message["flowId"]
            status = message["status"]
            proxyUsers = message["proxyUsers"]
            text = """1.29 azkaban报警： {} {} at {} is {}""".format(projectName, flowId, updateTime, status)
            msg(text)
        except:
            print("1.29 no alert")
