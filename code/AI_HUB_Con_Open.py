############################# OPEN DIALOG
# -*- coding:utf-8 -*-
import urllib3
import json
import re

openApiURL = "http://aiopen.etri.re.kr:8000/Dialog"
accessKey = "cc6f69e3-4af7-405e-b286-985536c960c4"
access_method = "internal_data"
method = "open_dialog"
name = "AI_chat"

def Open():

    requestJson = {
        "access_key": accessKey,
        "argument": {
            "name": name,
            "method": method,
            "access_method": access_method
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
    #print("대화 오픈")
    #print(str(response.data, "utf-8"))
    text_data = str(response.data, "utf-8")
    uuid = "617208326861624290"
    system_text = text_data
    print("System Log: ", system_text)
    try:
        uuid = re.search('"uuid":"(.+?)","result":', text_data).group(1)
        system_text = system_text.replace('{"result":0,"return_object":{"method":"open_dialog","uuid":"'+uuid+'","result":{"system_text":"', "")
        system_text = system_text.replace('\\n","state":"start","message":""}}}', "")
    except AttributeError:
        pass

    #print(text_data)
    #print(uuid)
    #print(system_text)
    #uuid =
    #uuid =
    return system_text, uuid