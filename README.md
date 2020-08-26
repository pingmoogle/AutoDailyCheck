# AutoDailyCheck
每日自动晨午晚检，解放双手~  
Powered by Python + Flask

## 立即上手
❤ [DEMO](https://soowin.me)

## Debug方法
1. Checkout codes
2. Requirements： Python3 and Linux OS (Not supported on Windows when using gunicorn)
0. Create a new file "users.json" in sever folder.  
Format like this:  
 {"ID1":"password2", "ID2":"Password2"}
3. execute ```python3 -m pip install -r requirements.txt```
4. execute ```python3 -m flask run -h Host -p Port```

You can also uncomment the main function in app.py and run
```python3 app.py```


## 性能突破
由于本身性能的问题，Flask 并不适合直接用作web 服务器，常见的方案是使用Flask+gunicorn+nginx
gunicorn 配合gevent 可以高效代理WSGI应用程序
```shell script
gunicorn -c config.py app:app
```
也可以使用PythonAnyWhere、Heroku、Azure等部署，详情参考：[Deployment Options](https://flask.palletsprojects.com/en/1.1.x/deploying/)
