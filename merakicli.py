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
    #print (mget.url)
    if int(mget.status_code) == 404:
        return '{"status":"page does not exist"}'
    else:
        return json.dumps(mget.json())
def merakiPut(merakiJson, path):
    mput = requests.put(baseAPI + path, data=merakiJson, headers=headers)
    if mput.status_code != 200:
        return '{"status":"error"}'
    else:
        return json.dumps(mput.json())
def merakiPost(merakiJson, path):
    return requests.post(baseAPI + path, data=merakiJson, headers=headers)
def merakiDel():
    pass

#CLI parsing
if sys.argv[1] == 'get':
    for arg in sys.argv[2:]:
        totalarg = totalarg + arg
        # Parse last slash out
        if arg != sys.argv[-1]:
            totalarg = totalarg + "/"
    print(merakiGet(totalarg))
if sys.argv[1] == 'put':
    for arg in sys.argv[3:]:
        totalarg = totalarg + arg + "/"
    result = merakiPut(json.loads(sys.argv[2]), totalarg)
    print(result)
if sys.argv[1] == 'post':
    for arg in sys.argv[3:]:
        totalarg = totalarg + arg + "/"
    result = merakiPost(sys.argv[2], totalarg)
    print(result)


