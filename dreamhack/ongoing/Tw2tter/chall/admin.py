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


if __name__ == '__main__': # 이 뜻은 __name__이 __main__이어야 한다는 뜻이다 쉽게 설명하자면 python3 admin.py로 실행하면 __name__은 __main__이 되고
	# test.py에서 import admin.py를 불러와서 실행하면 __name__은 test로 설정이 된다. 그러니깐 직접적으로 admin.py를 실행 시킬 때만 이 코드를 실행시키라는 말이다. 
    wait_server()
    with requests.Session() as session: # requests.Session()을 session이라는 이름으로 사용하겠다.
        admin_auth_data = {
            'username': 'admin',
            'password': environ.get('ADMIN_PASSWORD'),
        }
        while True:
            try:
                result = get_reports(session, admin_auth_data)
                report_ids = [report.get('id') for report in result.get('data').get('reports')]
                for report_id in report_ids:
                    result = accept_report(session, admin_auth_data, report_id)
            except Exception:
                pass
            sleep(5)
