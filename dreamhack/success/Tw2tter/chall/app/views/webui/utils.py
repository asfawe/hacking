from dataclasses import dataclass, fields
from functools import wraps
from flask import render_template, session, redirect
from app.components.post import get_post as get_post_from_db, get_posts as get_posts_from_db


def render_template_wrapper(template, **kwargs):
    return render_template(template, authenticated=session.get('authenticated'), **kwargs)


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('authenticated'):
            return func(*args, **kwargs)
        else:
            return redirect('/auth/login')
    return wrapper


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('authenticated') and is_admin(session):
            return func(*args, **kwargs)
        else:
            return redirect('/auth/login')
    return wrapper


@dataclass
class Permission:
    # None: Any
    read: bool = False
    # None: Any
    write: bool = False

    def __le__(self, other):
        assert isinstance(other, Permission)
        # True <= False
        def le(elem1, elem2):
            return elem2 is False or elem1 == elem2
        return all(
            le(getattr(self, field.name), getattr(other, field.name))
            for field in fields(self)
        )


def is_admin(session):
    return session.get('user_id') == 1


def permission_for_post(session, post): # 요청한 게시물 글? 의 권한이 있는지 확인
    permission = Permission() # 그냥 오리지날 Permission은 read = False, write = False
    user_id = session.get('user_id')
    if is_admin(session) or user_id == post.author_id or not post.hidden:	
        permission.read = True
    if is_admin(session) or user_id == post.author_id: # 지금 로그인 한 user와 글을 쓴 user와 똑같냐?
        permission.write = True
    return permission


def get_post(session, post_id, permission=Permission()):
    post = get_post_from_db(post_id)
    if post != None and permission_for_post(session, post) <= permission:
        return post
    else:
        return None


def get_posts(session, permission=Permission()):
    posts = get_posts_from_db() # 요청한 게시물 글?을 posts로
    return filter(lambda post: permission_for_post(session, post) <= permission, posts)
	# posts값이 post로
	# 만약 요청한 게시글의 권한보다 user의 권한이 같거나 크면 보여줌.
	# 만약 admin 게시물과 write 권한을 요청했다면 guest로는 write가 안되기 때문에 바로 빠꾸!
	# 권한 확인 후 알 맞는 게시물 보여주기 & 쓰기 가능하게 하기
