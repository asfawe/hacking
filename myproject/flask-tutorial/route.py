from flask import Blueprint

bp = Blueprint('webui', __name__)

@bp.route('/')
def index():
	return "<h1>Web UI</h1>"