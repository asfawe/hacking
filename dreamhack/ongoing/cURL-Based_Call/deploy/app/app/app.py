#!/usr/bin/env python3
import json
import pprint
import subprocess
from flask import Flask, redirect, request, abort, render_template, url_for, g

POST = 'POST'
GET = 'GET'
PATCH = 'PATCH'
DELETE = 'DELETE'

BACKEND_BASE_URL = 'http://backend:8000'


app = Flask(__name__)


def curl_backend_api(path, method, client_host, token=None, data=None):
    try:
        args = [ # '/usr/bin/curl' == curl
				 # 그냥 설치 경로 위치에서 curl을 실행시킨 거임.
            '/usr/bin/curl', f'{BACKEND_BASE_URL}{path}',
            '-H', f'Simple-Token: {token}',
            '-H', f'X-Forwarded-For: {client_host}', # 여기서 X-Forwarded-For의 client의 ip를 넣어주는 군...
            '-H', 'Content-Type: application/json',
            '-X', method,
            '--ignore-content-length',
            '--max-time', '0.3',
            '-d', json.dumps(data) if data else ''
        ]
        res = subprocess.run(args, capture_output=True)
		# capture_output는 출력 결과를 화면에 출력 해주기 위해 있는거임.
		# 그래서 res 값이 들어갈 수 있는 거임.
		# subprocess.run() 는 시스템?? 명령어를 실행할 수 있게 해주는 놈입니다.
		# 예를 들면 ls, cat, curl 등등
        return res.stdout.decode() # curl에서 출력한 걸 문자열로 return 해준다.
		# 만약 subprocess.run에 ls를 적었다고 치면 이런 식으로 반환됨.
		# stdout: b'app.py\nrun.sh\nrequirements.txt\n 등등'
		# 근데 이렇게 나오면 보기 힘들기 때문에 그걸 디코드에 해서 보기 쉽게 바꾼 거임.
    except: # 만약 실행 실패를 했다면 None를 반환합니다.
        return None

def beautify(res): # 예쁘게 json파일을 파이썬 딕셔너리로 만드는 함수.
    r = pprint.pformat(json.loads(res))
    return r


@app.before_request # 말 그대로 http 요청 가기전에 먼저 밑에 함수가 실행되게 하는 거임.
def before_request():
    if request.path != '/' and not request.path.startswith('/static/'):
        g.simple_token = request.args.get('simple_token')
		# 여기서 g는 global 공간이라고 보면 된다.
        if g.simple_token is None:
            abort(401)

@app.route('/', methods=['GET'])
def get_index():
    res = curl_backend_api('/auth', POST, request.remote_addr) # token을 만들어 주면서 뭐 여러가지 하는 것 같음.

    simple_token = json.loads(res) # json.loads는 json 형식을 python 딕셔너리 형태로 만들기 위한 거다.

    return redirect(url_for('get_menu', simple_token=simple_token))

@app.route('/menu', methods=['GET'])
def get_menu():
    return render_template('menu.html', simple_token=g.simple_token) # 이쪽까지는 그냥 기본 설정임.

@app.route('/create', methods=['GET'])
def get_create():
    return render_template('create.html', simple_token=g.simple_token)

@app.route('/create', methods=['POST'])
def post_create():
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')

    if not isinstance(title, str) \
            or not isinstance(content, str) \
            or not isinstance(author, str):
        abort(400) # 입력 받는 title, content, author가 str인지 확인

    data = {'title': title, 'content': content, 'author': author} # 그 후 json 형태로 바꿔서 넣기
    res = curl_backend_api('/posts', POST, request.remote_addr, g.simple_token, data)
    if res is None:
        abort(400)

    return render_template('/api_result.html', simple_token=g.simple_token, res=beautify(res))

@app.route('/read', methods=['GET'])
def get_read():
    res = curl_backend_api('/posts', GET, request.remote_addr, g.simple_token)
    if res is None:
        abort(400)

    return render_template('/api_result.html', simple_token=g.simple_token, res=beautify(res))

@app.route('/update', methods=['GET'])
def get_update():
    return render_template('update.html', simple_token=g.simple_token)

# 여기서 버프슈트로 POST 요청에서 PUT으로 변경해서 전송하려고 했는데... 
# 근데 중요한건 우리는 지금 이 밑에 함수를 들어갈 때 요청을 바꾸는 거임...
# curl_backend_api가 아닌...
@app.route('/update', methods=['POST'])
def post_update():
    post_idx = request.form.get('post_idx')
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')

    if not isinstance(post_idx, str) \
            or not post_idx.isdecimal() \
            or not isinstance(title, str | None) \
            or not isinstance(content, str | None) \
            or not isinstance(author, str | None):
        abort(400)

    data = {'title': title, 'content': content, 'author': author}
    res = curl_backend_api(f'/posts/{post_idx}', PATCH, request.remote_addr, g.simple_token, data)
    if res is None:
        abort(400)

    return render_template('/api_result.html', simple_token=g.simple_token, res=beautify(res))

@app.route('/delete', methods=['GET'])
def get_delete():
    return render_template('delete.html', simple_token=g.simple_token)

@app.route('/delete', methods=['POST'])
def post_delete():
    post_idx = request.form.get('post_idx')
    if not isinstance(post_idx, str) or not post_idx.isdecimal():
        abort(400)

    res = curl_backend_api(f'/posts/{post_idx}', DELETE, request.remote_addr, g.simple_token)
    if res is None:
        abort(400)

    return render_template('/api_result.html', simple_token=g.simple_token, res=res)
