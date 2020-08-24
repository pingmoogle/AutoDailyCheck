# -*- coding: UTF-8 -*-

import json
import requests
import time


def sendMail(msgtext, useraddr):
    pass


if __name__ == '__main__':

    # Prepare
    data = {}
    with open("data.json", "r") as fd:
        data = json.load(fd)
    users = {}
    with open("users.json", "r") as ufd:
        users = json.load(ufd)

    for u, p in users.items():
        with open("../logs/"+u+".log", "a") as logfd:
            uname = u
            upswd = p
            # Login
            conn = requests.Session()
            result = conn.post(
                url="https://xxcapp.xidian.edu.cn/uc/wap/login/check",
                data={'username': uname, 'password': upswd}
            )
            if result.status_code != 200 or "账号或密码错误" in result.text:
                # print('Failed to login.', result.status_code)
                logfd.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\tFailed to login.<br>\n")
                conn.close()
                continue

            # Post
            result = conn.post(
                url="https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save",
                data=data
            )
            if result.status_code != 200:
                # print("Error.", result.status_code)
                logfd.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\tFailed to connect<br>\n")
                conn.close()
                continue

            # Result
            rjson = json.loads(result.text)
            # print(rjson['m'])
            logfd.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\t"+rjson["m"]+"<br>\n")
            conn.close()
