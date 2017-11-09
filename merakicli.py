import requests
import os
import sys
import json

totalarg = ""
merakiURL = {
    "base": "dashboard.meraki.com",
    "API": "/api/v0/"
}

headers = {
    "X-Cisco-Meraki-API-Key": os.environ['merakiapi']
}

baseAPI = "https://" + merakiURL.get('base') + merakiURL.get('API')


def merakiGet(path):
    mget = requests.get(baseAPI + path, headers=headers)
    return json.dumps(mget.json())
def merakiPut(merakiJson, path):
    return requests.put(baseAPI + path, data=merakiJson, headers=headers)
def merakiPost(merakiJson, path):
    return requests.post(baseAPI + path, data=merakiJson, headers=headers)
def merakiDel():
    pass


if sys.argv[1] == 'get':
    for arg in sys.argv[2:]:
        totalarg = totalarg + arg + "/"
    print(merakiGet(totalarg))
if sys.argv[1] == 'put':
    for arg in sys.argv[3:]:
        totalarg = totalarg + arg + "/"
    result = merakiPut(json.loads(sys.argv[2]), totalarg)
    print (totalarg)
    print (sys.argv[2])
    print(result)
if sys.argv[1] == 'post':
    for arg in sys.argv[3:]:
        totalarg = totalarg + arg + "/"
    result = merakiPost(sys.argv[2], totalarg)
    print(result)

