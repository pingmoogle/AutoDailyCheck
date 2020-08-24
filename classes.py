# -*- encoding: UTF-8 -*-

import json

import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import *


class NameForm(FlaskForm):
    name = StringField("Your ID: ", validators=[DataRequired(), Length(11)])
    pswd = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class Check():
    def checkIDResult(uid, pswd):
        conn = requests.Session()
        result = conn.post(
            url="https://xxcapp.xidian.edu.cn/uc/wap/login/check",
            data={'username': uid, 'password': pswd}
        )
        if result.status_code != 200 or "账号或密码错误" in result.text:
            conn.close()
            return False
        else:
            conn.close()
            return True

    def checkIDResult2(uid, pswd):
        return True

    def userInJson(uid, pswd):
        users = {}
        with open("server/users.json", "r") as ufd:
            users = json.load(ufd)
        if uid in users.keys() and users[uid] == pswd:
            return True
        elif uid in users.keys() and users[uid] != pswd:
            Execute.insertThisUser(uid, pswd)
            return True
        else:
            return False


class Execute():
    def insertThisUser(uid, pswd):
        with open("server/users.json", "r") as fd:
            user = json.load(fd)
            fd.close()
        user[uid] = pswd

        with open("server/users.json", "w+") as fd:
            fd.seek(0)
            json.dump(user, fd)
            fd.close()
