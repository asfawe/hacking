from flask import Flask
from route import bp as bp_webui

app = Flask(__name__) # 현재 모듈을 기반으로 한 Flask 애플리케이션 객체를 생성하는 것

if __name__ == '__main__':
	app.register_blueprint(bp_webui)
	app.run(host='127.0.0.1', port=3000)

