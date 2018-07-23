from flask import Flask
from config import DEBUG
# 实例化flask
app = Flask(__name__)
# 载入配置文件
app.config.from_object('config')


# 第一种注册路由的方式
@app.route("/")
def home():
    # 1/0
    return 'Hello, Flask!'

# 第二种注册路由的方式
# app.add_url_rule('/home',view_func=home)


if __name__ == '__main__':
    # 一个python的文件有两种使用的方法，第一是直接作为脚本执行，第二是import到其他的python脚本中被调用（模块重用）执行
    # if __name__ == '__main__'的意思是：当.py文件被直接运行时(开发环境)，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时（生产环境，nginx+uwsgi），if __name__ == '__main__'之下的代码块不被运行。
    app.run(host='0.0.0.0',port=80,debug=app.config['DEBUG'])
    # 开启调试模式可以自动重启服务器