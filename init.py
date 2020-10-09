import json
import pyotp
import requests
import base64


def parse_url(url):
    code, hostb64 = url.split('?value=')[1].split('-')                                
    host = base64.b64decode(hostb64 + '='*(-len(hostb64) % 4)).decode("utf-8")
    activation_url = "https://" + host + "/push/v2/activation/" + code
    return activation_url

def activate(url):
    print(url)
    res = requests.post(url)
    res = json.loads(res.text)
    print(res)
    key = res['response']['hotp_secret']
    return key

def init():
    with open("secret.conf", 'r') as file:
        cfg = json.loads(file.read())
        url = cfg["url"]
        key = activate(parse_url(url))
        cfg["key"] = base64.b32encode(key.encode("utf-8")).decode()
        cfg["count"] = 0
        print(cfg)
    with open("secret.conf", 'w') as file:
        file.write(json.dumps(cfg))
    print("success!")
    input('Press ENTER to exit')

init()
