import json
import pyotp.hotp
import pyperclip

def get_key():
    with open("secret.conf", 'r') as file:
        cfg = json.loads(file.read())
        cfg["count"] += 1
    with open("secret.conf", 'w') as file:
        file.write(json.dumps(cfg))
    return cfg["key"].encode(), cfg["count"]

def get_hotp(key, count):
    hotp = pyotp.HOTP(key)
    passcode = hotp.at(count)
    return passcode

def main():
    key = get_hotp(*get_key())
    pyperclip.copy(key)


main()

