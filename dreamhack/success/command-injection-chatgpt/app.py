#!/usr/bin/env python3
import subprocess

from flask import Flask, request, render_template, redirect

from flag import FLAG

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        host = request.form.get('host')
        cmd = f'ping -c 3 {host}'
        try:
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
			# Bash에서 -c 옵션은 문자열을 인자로 받아 해당 문자열을 Bash 명령어로 해석하여 실행하는 데 사용됩니다. -c를 사용하면, 스크립트 파일 없이 직접 명령어를 실행할 수 있습니다.
            return render_template('ping_result.html', data=output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return render_template('ping_result.html', data='Timeout !')
        except subprocess.CalledProcessError:
            return render_template('ping_result.html', data=f'an error occurred while executing the command. -> {cmd}')

    return render_template('ping.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
