# -*- coding: utf-8 -*-
from fastapi import FastAPI
from db import session  # DBと接続するためのセッション
from model import UserTable  # Userテーブルのモデル


# fastapiでエンドポイントを定義するために必要
app = FastAPI()

# ユーザ情報を返す GET
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    # DBからuser_idを元にユーザを検索
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    # ユーザが見つからなかった場合
    if (user is None):
        return {"code": 404, "message": "User Not Found"}
    return user

# ユーザ情報を登録 POST
@app.post("/users")
# クエリでnameとageを受け取る
async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()
