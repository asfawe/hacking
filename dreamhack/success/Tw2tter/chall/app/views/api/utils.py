from dataclasses import asdict, dataclass, fields
from functools import wraps
import json
from flask import Response, request
from app.components.post import get_post as get_post_from_db, get_posts as get_posts_from_db


@dataclass
class ApiResponse:
    success: bool
    data: dict

    def __dict__(self):
        return asdict(self)
    
    def json(self):
        return json.dumps(self.__dict__())
    

def fail():
    raise Exception


def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.form.get('token'):
            return func(*args, **kwargs)
        else:
            return ApiResponse(False, {}).json()
    return wrapper


def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            r = func(*args, **kwargs)
            if r is None:
                r = ApiResponse(False, {}).json()
        except Exception:
            r = ApiResponse(False, {}).json()
        return Response(r, mimetype='application/json')
    return wrapper


@dataclass
class Permission:
    # None: Any
    read: bool = False
    # None: Any
    write: bool = False

    def __le__(self, other): 
		# __le__는 python에서 매직 메서드라고 합니다. 
		# 만약 Permission 인스턴스끼리 비교 연산자 나오면 바로 실행되는 함수입니다.

        assert isinstance(other, Permission)
        # True <= False
        def le(elem1, elem2):
            return elem2 is False or elem1 == elem2
        return all(
            le(getattr(self, field.name), getattr(other, field.name))
            for field in fields(self)
        )
#####################################

          # example code #

# class MyNumber:
#     def __init__(self, value):
#         self.value = value

#     def __le__(self, other):
#         if isinstance(other, MyNumber):
#             return self.value <= other.value
#         else:
#             raise TypeError("Unsupported type for comparison")

# num1 = MyNumber(1)
# num2 = MyNumber(2)
# print(num1 <= num2)  # 출력: True

# 여기서 num1 <= num2를 실행하면, 사실은 num1.__le__(num2)를 호출하는 것과 같습니다. 
# 여기서 num1이 self가 되고, num2가 other가 됩니다. 
# 이 메서드는 self 즉 num1이 other 즉 num2보다 작거나 같은지 (self.value <= other.value)를 판별하고 결과를 반환합니다.

# 따라서 other는 <= 연산자를 사용하여 self와 비교되는 객체를 나타냅니다.

#####################################

def is_admin(api_token):
    return api_token.is_admin


def permission_for_post(api_token, post):
    permission = Permission()
    if api_token.is_admin or api_token.user_id == post.author_id or not post.hidden:
        permission.read = True
    if api_token.is_admin or api_token.user_id == post.author_id:
        permission.write = True
    return permission


def get_post(api_token, post_id, permission=Permission()):
    post = get_post_from_db(post_id)
    if post != None and permission_for_post(api_token, post) <= permission:
        return post
    else:
        return None


def get_posts(api_token, permission=Permission()):
    posts = get_posts_from_db()
    return filter(lambda post: permission_for_post(api_token, post) <= permission, posts)
