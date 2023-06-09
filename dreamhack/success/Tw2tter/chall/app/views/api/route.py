
from flask import Blueprint, request
from app.components.post import add_post, remove_post
from app.components.user import get_user, get_user_by_username_and_password
from app.components.report import get_reports, add_report, remove_report, get_report
from app.components.api_token import create_token, validate_token, remove_token, get_token, validate_token_admin
from app.views.api.utils import ApiResponse, Permission, json_response, require_token, get_posts, get_post, fail


bp = Blueprint('api', __name__) 
# Blueprint를 사용하면 Flask 애플리케이션의 라우트와 기타 코드를 모듈화하고 재사용할 수 있어, 애플리케이션의 구조와 유지 관리를 훨씬 쉽게 만들 수 있습니다.
# 첫 번째 아규먼트는 blueprint의 이름이고 두 번째 아규먼트는 blueprint가 정의된 Python 모듈의 이름입니다. 
# Flask는 이 정보를 사용하여 blueprint와 관련된 리소스를 찾습니다.
# 세 번째 아규먼트도 지정할 수 있지만 지정하지 않으면 자동으로 '/'로


@bp.route('/api/auth', methods=['POST'])
@json_response
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    if not (username and password):
        fail()

    user = get_user_by_username_and_password(username, password)
    token = create_token(user.id)
    return ApiResponse(True, {'token': token}).json()


@bp.route('/api/post', methods=['POST'])
@json_response
@require_token
def post_get():
    token = request.form.get('token')
    post_id = request.form.get('post_id')

    if not validate_token(token):
        fail()

    api_token = get_token(token)

    if post_id:
        post = get_post(api_token, post_id, Permission(read=True))
        post = {
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
        }
        remove_token(token)
        return ApiResponse(True, {'post': post}).json()
    else:
        posts = get_posts(api_token, Permission(read=True))
        posts = [{
            'id': post.id,
            'title': post.title,
            'author': post.author.username,
        } for post in posts]
        remove_token(token)
        return ApiResponse(True, {'posts': posts}).json()


@bp.route('/api/post/create', methods=['POST'])
@json_response
@require_token
def post_create():
    token = request.form.get('token')
    title = request.form.get('title')
    content = request.form.get('content')

    if title is None or content is None:
        fail()

    if validate_token(token):
        api_token = get_token(token)
        add_post(title, content, api_token.user_id)
        remove_token(token)
        return ApiResponse(True, {}).json()


@bp.route('/api/post/report', methods=['POST'])
@json_response
@require_token
def post_report():
    token = request.form.get('token')
    post_id = request.form.get('post_id')
    reason = request.form.get('reason')

    if post_id is None or reason is None:
        fail()
    if not validate_token(token):
        fail()
    
    api_token = get_token(token)

    if get_post(api_token, post_id) is None:
        fail()
    
    add_report(post_id, reason, api_token.user_id)
    remove_token(token)
    return ApiResponse(True, {}).json()


@bp.route('/api/admin/report', methods=['POST'])
@json_response
@require_token
def admin_report_get():
    token = request.form.get('token')
    report_id = request.form.get('report_id')

    if not validate_token_admin(token):
        fail()

    api_token = get_token(token)

    if report_id: # admin에서 get_repots로 요청했을 때 id를 같이 안 보내줬기 때문에 else문으로~ gogo~
        report = get_report(report_id)
        post = get_post(api_token, report.post_id)
        report = {
            'post_id': report.post_id,
            'post_title': post.title,
            'post_content': post.content,
            'reason': report.reason,
            'reporter': get_user(report.reporter_id).username,
        }
        remove_token(token)
        return ApiResponse(True, {'report': report}).json()
    else: # 모든 신고 내역 받아오기~ admin은 최고 권력자~
        reports = [{
            'id': report.id,
            'post_title': get_post(api_token, report.post_id).title,
            'reason': report.reason,
            'reporter': get_user(report.reporter_id).username,
        } for report in get_reports() if get_post(api_token, report.post_id)]
        remove_token(token)
        return ApiResponse(True, {'reports': reports}).json()


@bp.route('/api/admin/report/decline', methods=['POST'])
@json_response
@require_token
def admin_report_decline():
    token = request.form.get('token')
    report_id = request.form.get('report_id')
    
    if not report_id or not validate_token_admin(token):
        fail()
    
    report = get_report(report_id)
    if report:
        remove_report(report_id)
        remove_token(token)
        return ApiResponse(True, {}).json()
    else:
        fail()


@bp.route('/api/admin/report/accept', methods=['POST'])
@json_response
@require_token
def admin_report_accept():
    token = request.form.get('token')
    report_id = request.form.get('report_id')

    if not report_id or not validate_token_admin(token):
        fail()

    accepted_report = get_report(report_id)
    remove_post(accepted_report.post_id)
    duplicate_reports = filter(
        lambda report: report.post_id == accepted_report.post_id,
        get_reports()
    )
    for report in duplicate_reports:
        remove_report(report.id)

    remove_token(token)
    return ApiResponse(True, {}).json()
