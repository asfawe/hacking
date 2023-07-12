from __future__ import annotations
import time
import os
from uuid import UUID, uuid4
from flask import Flask, render_template, request, redirect, url_for, abort
from utils import set_attr
import hashlib
from typing import Dict

class Password:
    data: str

    def __init__(self, data: str) -> None:
        self.data = hashlib.sha256(data.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.data == hashlib.sha256(password.encode()).hexdigest()


class Title:
    data: str
    edit_time: float

    def __init__(self, data: str) -> None:
        self.data = data
        self.edit_time = time.time()

    def get_raw_data(self):
        return self.data.strip()

    def get_title(self):
        return "Title: {0:<10}".format(self.data.strip())

    def get_title_with_edit_time(self):
        return "Title: {0:<10} (edited: {1})".format(
            self.data.strip(),
            time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(self.edit_time)),
        )


class Content:
    data: str
    edit_time: float

    def __init__(self, data: str) -> None:
        self.data = data
        self.edit_time = time.time()

    def get_raw_data(self):
        return self.data.strip()

    def get_content(self):
        return "Content: {0:<10}".format(self.data.strip())

    def get_content_with_edit_time(self):
        return "Content: {0:<10} (edited: {1})".format(
            self.data.strip(),
            time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(self.edit_time)),
        )


class Memo:
    collections: Dict[str, Memo] = {}

    title: Title
    content: Content
    password: Password

    def __init__(self, title: str, content: str, password: str):
        self.id = str(uuid4())
        self.title = Title(title)
        self.content = Content(content)
        self.password = Password(password)

    def get_raw_title(self):
        return self.title

    def get_raw_content(self):
        return self.content

    def get_title(self):
        return self.title.get_title()

    def get_content(self):
        return self.content.get_content()

    def get_title_with_edit_time(self):
        return self.title.get_title_with_edit_time()

    def get_content_with_edit_time(self):
        return self.content.get_content_with_edit_time()

    def check_password(self, password):
        return self.password.check_password(password)

    @staticmethod
    def get_memo_by_id(memo_id: str) -> Memo | None:
        print(memo_id)
        return Memo.collections[memo_id] if memo_id in Memo.collections.keys() else None
        

    @staticmethod
    def add_memo_to_collection(memo: Memo):
        print(memo.id)
        print(memo.title.data)
        Memo.collections[memo.id] = memo
    # print(Memo.collections.keys())

def set_attr(obj, prop, value):
    prop_chain = prop.split('.')
    cur_prop = prop_chain[0]
    if len(prop_chain) == 1:
        if isinstance(obj, dict):
            obj[cur_prop] = value
        else:
            setattr(obj, cur_prop, value)
    else:
        if isinstance(obj, dict):
            if  cur_prop in obj:
                next_obj = obj[cur_prop]
                # print("hahah")
            else:
                next_obj = {}
                obj[cur_prop] = next_obj
        else:
            if hasattr(obj, cur_prop):
                next_obj = getattr(obj, cur_prop)
            else:
                next_obj = {}
                setattr(obj, cur_prop, next_obj)
        print(next_obj)
        set_attr(next_obj, '.'.join(prop_chain[1:]), value)

def get_memo_with_auth_or_abort(memo_id: str, password: str) -> Memo:
    memo = Memo.get_memo_by_id(memo_id)

    if memo is None:
        abort(404)
    elif not memo.check_password(password):
        abort(403)

    return memo

password2 = os.urandom(20).hex()

secret = Memo("secret", open("../flag", "r").read(), password2)
# print(secret.password.data)
# print(hashlib.sha256(password2.encode()).hexdigest())
Memo.add_memo_to_collection(secret)

app = Flask(__name__)


@app.route("/")
def index():
    memo_title_list = [
        (memo.id, memo.get_title()) for memo in Memo.collections.values()
    ]

    return render_template("index.html", memos=memo_title_list)


@app.route("/new", methods=["GET", "POST"])
def new_memo():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        password = request.form["password"]

        Memo.add_memo_to_collection(Memo(title, content, password))

        return redirect(url_for("index"))
    return render_template("new_memo.html")


@app.route("/edit/<uuid:memo_id>", methods=["GET", "POST"])
def edit_memo(memo_id: UUID):
    print(secret.password.data)
    memo_id = str(memo_id)

    if request.method == "GET":
        return render_template("edit_memo.html", memo_id=memo_id)
    elif request.method == "POST":
        selected_option = request.form["selected_option"]
        edit_data = request.form["edit_data"]
        password = request.form["password"]

        memo = get_memo_with_auth_or_abort(memo_id, password)

        set_attr(memo, selected_option + ".data", edit_data)
        set_attr(memo, selected_option + ".edit_time", time.time())

        return redirect(url_for("index"))


@app.route("/view/<uuid:memo_id>", methods=["GET", "POST"])
def view_memo(memo_id: UUID):
    memo_id = str(memo_id)

    if request.method == "GET":
        return render_template("enter_password.html", memo_id=memo_id)
    elif request.method == "POST":
        password = request.form["password"]

        memo = get_memo_with_auth_or_abort(memo_id, password)

        contents = (
            memo.get_title_with_edit_time() + "\n" + memo.get_content_with_edit_time()
        )

        return render_template("view_memo.html", memo=contents, memo_id=memo_id)


if __name__ == "__main__":
    app.run(debug=False)
