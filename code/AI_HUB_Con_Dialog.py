############################# DIALOG
# -*- coding:utf-8 -*-
import urllib3
import json
import re

openApiURL = "http://aiopen.etri.re.kr:8000/Dialog"
accessKey = "cc6f69e3-4af7-405e-b286-985536c960c4"
method = "dialog"

def Dialog(text_data, uuid):
    text = text_data
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "method": method,
            "text": text,
            "uuid": uuid
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )


    #print("[responseCode] " + str(response.status))
    #print("[responBody]")
    #print("대화")
    #print(str(response.data, "utf-8"))
    text_data = str(response.data, "utf-8")
    system_text = text_data
    print("System Log: ", system_text)
    system_text = system_text.replace('{"result":0,"return_object":{"method":"dialog","uuid":"' + uuid + '","result":{"system_text":"', "")
    system_text = system_text.replace('\\n","state":"dialog","message":""}}}', "")
    #print(system_text)

    try:
        system_text = system_text.replace('(', "")
        system_text = system_text.replace(')', "")
        system_text = re.search('chat(.+?)/chat', system_text).group(1)
    except:
        pass

    #print(system_text)

    return system_text