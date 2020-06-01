import requests
import base64
import time
import json

# 图片名
imageName = "D:/CCTVlook/shot0.jpg"

# 请求地址
host = "http://localhost:8081"
endpoint = r"/image"

url = ''.join([host, endpoint])


# 获取header
def getHeader():
    curTime = str(int(time.time()))

    # 组装http请求头
    header = {
        'CurTime': curTime,
        'Message': 'Test Post From postImage.py',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    return header


# 获取body
def getBody(filepath):
    with open(filepath, 'rb') as f:
        imgfile = f.read()
    data = {
        'name': imageName,
        'imageBase64': str(base64.b64encode(imgfile), 'utf-8')
    }
    return data


r = requests.post(url, headers=getHeader(), data=json.dumps(getBody(imageName)))

# 返回信息
print(r.text)
