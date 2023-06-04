import os
from datetime import datetime
from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

with open('../flag', 'r') as f:
    FLAG = f.read()

class Post(BaseModel):
    idx: int
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: datetime

class PostCreate(BaseModel):
    title: str
    content: str
    author: str

class PostUpdatePut(BaseModel):
    title: str
    content: str
    author : str

class PostUpdatePatch(BaseModel):
    title: str | None = None
    content: str | None = None
    author : str | None = None


simple_tokens = []
posts = {}
next_post_idx = 0

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)


def process_post_creation(post_create: PostCreate):
    global next_post_idx
    global posts
    post = Post(
        idx=next_post_idx,
        title=post_create.title,
        content=post_create.content,
        author=post_create.author,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    posts[next_post_idx] = post
    next_post_idx += 1
    return post

def process_post_full_update(post_idx, post_update_put: PostUpdatePut):
    global posts
    post = posts[post_idx]
    post.title = post_update_put.title
    post.content = post_update_put.content
    post.author = post_update_put.author
    post.updated_at = datetime.now()
    return post

def process_post_partial_update(post_idx, post_update_patch: PostUpdatePatch):
    global posts
    post = posts[post_idx]
    if post_update_patch.title:
        post.title = post_update_patch.title
    if post_update_patch.content:
        post.content = post_update_patch.content
    if post_update_patch.author:
        post.author = post_update_patch.author
    post.updated_at = datetime.now()
    return post

# 그러니깐 결국에는 app.py(client)에서 curl로 http://backend:8000을 보냈을 때
# 여기서 작업해주는 거임.
@app.middleware('http')
async def verify_user(request: Request, call_next):
    if request.url.path != '/auth':
        if request.headers.get('Simple-Token') not in simple_tokens:
            return JSONResponse(status_code=401, content=None)
    response = await call_next(request)
	# 위 구문을 사용하는 이유 
	# 간단히 정리하면, 클라이언트가 요청한 경로 작업 함수에서 반환하는 값이 최종적으로 클라언트에게 반환됩니다. 
	# 이 과정에서 미들웨어는 추가적인 작업(예: 사용자 인증 등)을 수행합니다. 
	# 일반적 경우에는 미들웨어에서 반환하는 값은 await call_next(request)에서 얻은 값과 동일합니다. 
	# 그러나 특별한 경우, 예를 들어 인증이 실패한 경우에는 미들웨어에서 적절한 예외응답 반환해 줄 수도 있습니다(예: 상태 코드 401).
    return response

@app.post('/auth')  # 처음에 token을 만드는 함수임.
async def issue_token():
    global simple_tokens
    simple_token = os.urandom(32).hex()
    simple_tokens.append(simple_token)
    return simple_token

@app.post('/posts')
async def create_post(post_create: PostCreate):
    return process_post_creation(post_create)
# 여기서 PostCreate는 Pydantic 모델 또는 데이터 클래스로 정의되어 있어야 합니다. 
# 이 클래스는 JSON 데이터를 파싱할 필드와 데이터 유형을 정의하며, 
# FastAPI는 이를 사용하여 HTTP 요청의 본문에서 데이터를 추출하고 PostCreate 객체를 생성합니다.

@app.get('/posts')
async def read_posts():
    return posts

# 그냥 해당하는 post_idx를 출력하는 거다.
@app.get('/posts/{post_idx}')
async def read_posts_by_post_idx(post_idx: int, response: Response):
    if post_idx in posts:
        return posts[post_idx]
    response.status_code = 404
    return None


@app.put('/posts/{post_idx}')
async def update_post_put(post_idx: int, post_update_put: PostUpdatePut, response: Response):
    global posts
    if post_idx in posts:
        return process_post_full_update(post_idx, post_update_put)
    response.status_code = 404
    return None

@app.delete('/posts/{post_idx}')
async def delete_post(post_idx: int, response: Response):
    global posts
    if post_idx in posts:
        del posts[post_idx]
        response.status_code = 204
        return None
    response.status_code = 404
    return None

@app.patch('/posts/{post_idx}')
async def update_post_patch(post_idx: int, post_update_patch: PostUpdatePatch, response: Response):
    global posts
    if post_idx in posts:
        return process_post_partial_update(post_idx, post_update_patch)
    response.status_code = 404
    return None

# 흠.. 그러면 결국에는 flag를 얻기 위해서는 127.0.0.1인 ip로 /admin 요청을 보내야 하는 거네?
@app.get('/admin')
async def get_admin(request: Request): # type hinting 이라고 그냥 request가 Request 타입이다. 라고 알려준거임.
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for != '127.0.0.1': # 여기서 가져온 X-Forwarded-For은 클라이언트의 ip 주소를 식별하기 위해 존재하는 놈입니다. 위에 app.py를 보면 이해가 되실겁니다.
		# 그러니깐 간단하게 설명을 하면 client의 ip를 가져오는 놈입니다.
        return JSONResponse(status_code=401, content=None)

    return {'message': FLAG} # json 표현법으로 나가야 하기 때문에 message: FLAG를 하면서 딕셔너리로 보내는 거임.

