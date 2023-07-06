from flask import Blueprint

bp = Blueprint('webui', __name__)
# Blueprint를 사용하면 Flask 애플리케이션의 라우트와 기타 코드를 모듈화하고 재사용할 수 있어, 애플리케이션의 구조와 유지 관리를 훨씬 쉽게 만들 수 있습니다.
# 첫 번째 아규먼트는 blueprint의 이름이고 두 번째 아규먼트는 blueprint가 정의된 Python 모듈의 이름입니다. 
# Flask는 이 정보를 사용하여 blueprint와 관련된 리소스를 찾습니다.
# 세 번째 아규먼트도 지정할 수 있지만 지정하지 않으면 자동으로 '/'로

@bp.route('/')
def index():
	return "<h1>Web UI</h1>"