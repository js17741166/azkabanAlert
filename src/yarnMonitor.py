# -*- coding: utf-8 -*-
# https://oapi.dingtalk.com/robot/send?access_token=18200f97032b410de1945348c80dcadad6b1a6d34ed3a1563d868b6abcba3472/
# https://oapi.dingtalk.com/robot/send?access_token=458b5f721ae67bedb8468315c1aa17e8c23298bfa3c166145285faed027f536a
# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import dateUtil
import datetime, time
headers = {'Content-Type': 'application/json;charset=utf-8'}
# yarn_app_url ="http://cdh2.car.bj2.yongche.com:8088/ws/v1/cluster/metrics"
yarn_application_running_url="http://cdh2.car.bj2.yongche.com:8088/ws/v1/cluster/apps?states=RUNNING"
ali_robot_url="https://oapi.dingtalk.com/robot/send?access_token=458b5f721ae67bedb8468315c1aa17e8c23298bfa3c166145285faed027f536a"
def getYarnApplicationRunning():
    req = requests.get(yarn_application_running_url, headers=headers, verify=False).content
    req_json = json.loads(req)
    if req_json.has_key("apps"):
        apps = req_json["apps"]
        apps_json = apps["app"]
        for i in apps_json:
            if i["user"] != "bigdata" and i["user"] != "lbsdata":
                user =i["user"]
                id=i["id"]
                trackingUrl=i["trackingUrl"]
                startedTime=i["startedTime"]
                name=i["name"]
                minueh=conculateTime(startedTime)
                if minueh>1:
                    text = """【集群1小时以上任务监控报警】{}的{}任务{}已经执行 {}小时以上，地址:{} """.format(user, id, name,minueh, trackingUrl)
                    msg(text)
                else:
                    return ""
    else:
        return ""
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
    print requests.post(ali_robot_url, json.dumps(json_text), headers=headers).content

def conculateTime(date2):
    currentDate = dateUtil.getCurrentDateTime()
    time_date = dateUtil.formatTimestamp(dateUtil.format_datetime, time.localtime(date2 / 1000))
    return dateUtil.dateDiffInSeconds(currentDate,time_date)/60/60

getYarnApplicationRunning()