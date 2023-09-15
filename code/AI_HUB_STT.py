# -*- coding:utf-8 -*-
import urllib3
import json
import base64
import os

openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "cc6f69e3-4af7-405e-b286-985536c960c4"
#audioFilePath = "output.wav"
languageCode = "korean"

def stt(audioFilePath):
    audioFilePath = "converse_recode/" + audioFilePath
    file = open(audioFilePath, "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()
    #os.remove(audioFilePath)

    requestJson = {
        "access_key": accessKey,
        "argument": {
            "language_code": languageCode,
            "audio": audioContents
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
    text_data = str(response.data, "utf-8")
    text_data = text_data.replace('{"result":0,"return_object":{"recognized":"', '')
    text_data = text_data.replace('"}}', '')
    print("User STT : ", text_data)
    if text_data == "ASR_NOTOKEN":
        return ""
    else:
        return text_data