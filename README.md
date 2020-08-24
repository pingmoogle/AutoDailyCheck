# AutoDailyCheck
每日自动晨午晚检，解放双手~  
Powered by Python + Flask

## 立即上手
❤ [DEMO](https://soowin.me)

## 构建方法
1. Checkout codes
2. Requirements： Python3 and Linux OS (Not supported on Windows when using gunicorn)
3. execute ```python3 -m pip install -r requirements.txt```
4. execute ```python3 -m flask run -h Host -p Port```

You can also uncomment the main function in app.py and run
```python3 app.py```


## 已知问题
由于本身性能的问题，Flask并不适合直接用作web服务器，常见的方案是使用Flask+gunicorn+nginx
