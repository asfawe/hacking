from os import environ
import requests
from time import sleep


HOST = 'http://localhost:55000'


def get_token(session, auth_data):
    sleep(0.1)
    return session.post(f'{HOST}/api/auth', data=auth_data).json().get('data').get('token')


def get_reports(session, auth_data):
    sleep(0.1)
    return session.post(f'{HOST}/api/admin/report', data={
        'token': get_token(session, auth_data),
    }).json()


def accept_report(session, auth_data, report_id):
    sleep(0.1)
    return session.post(f'{HOST}/api/admin/report/accept', data={
        'token': get_token(session, auth_data),
        'report_id': report_id,
    }).json()


def decline_report(session, auth_data, report_id):
    sleep(0.1)
    return session.post(f'{HOST}/api/admin/report/decline', data={
        'token': get_token(session, auth_data),
        'report_id': report_id,
    }).json()


def wait_server():
    while True:
        try:
            requests.get(HOST)
            break
        except requests.exceptions.ConnectionError:
            sleep(1)
            continue


if __name__ == '__main__':
    wait_server()
    with requests.Session() as session:
        admin_auth_data = {
            'username': 'admin',
            'password': environ.get('ADMIN_PASSWORD'),
        }
        while True:
            try:
                result = get_reports(session, admin_auth_data) # 모든 신고 내역을 받아옴
                report_ids = [report.get('id') for report in result.get('data').get('reports')]
				# result.get('data') 부분에 모든 정보들이 있음. 그 중에 reports 정보들도 있음.
				# 모든 신고를 하나씩 처리함
                for report_id in report_ids:
                    result = accept_report(session, admin_auth_data, report_id)
					# 아.아.아. 삭제 같은 요청들을 admin에서 해주고 그 api token이 검증에 실패해도 삭제되지 않음.
					# 그걸 이용하면 여러개의 admin의 api token을 만들 수 있음.
					# 그러면 api token 검정을 어떻게 실패하게 할까?
					# 만약 접수된 신고들이 모두 동일한 게시글에 대한 신고라면 첫 번째 API 호출에서 중복된 신고들이 모두 삭제됩니다. 
					# API 핸들러 admin_report_accept에서 이를 확인할 수 있습니다. 
					# 따라서 첫 호출을 제외한 모든 호출에서 get_report 함수로 신고를 받아올 때 None이 반환됩니다. 
					# 그 뒤 accepted_report.post_id에서 예외가 발생하고 토큰이 삭제되지 않은 채로 데이터베이스에 남게 됩니다.


            except Exception:
                pass
            sleep(5)
