"""

sudo vim /etc/nginx/sites-available/o821.com
gunicorn -w 4 -b 127.0.0.1:5001 main:app
京ICP备19017435号-1

环境依赖
    pip freeze > requirements.txt
    pip install -r requirements.txt
@app.route
    methods 指定请求方式
    <>包含路径参数值:path
实现状态保持主要有两种方式：
    在客户端存储信息使用Cookie
    在服务器端存储信息使用Session

上下文只有2种：
    1.request
    2.app对象

请求钩子：
    1.before_first_request第一次请求之前调用，初始化
    2.before_request在每一次请求之前调用，做请求的校
    3.after_request(响应)每一次请求之后，响应做最后一步统一的处理
    4.teardown_request(错误信息)每一次请求之后，参数是服务器出现的错误信息


sudo systemctl stop nginx
要再次启动，请键入：
sudo systemctl start nginx
重新启动Nginx服务：
sudo systemctl restart nginx
在进行一些配置更改后重新加载Nginx服务：
$sudo systemctl reload nginx
如果你想禁用Nginx服务在启动时启动：
$sudo systemctl disable nginx
并重新启用它：
$sudo systemctl enable nginx


ps aux | grep gunicorn
sudo vim /etc/nginx/sites-available/default
uwsgi --ini uwsgi.ini

gunicorn manage:app &
"""


from flask_6 import Flask, url_for  # 1.导入Flask类
from werkzeug.routing import BaseConverter  # 自定义路由转换
from flask_6 import request   # request获取参数 cookies / args
from flask_6 import jsonify   # 用于返回json数据
from flask_6 import redirect   # 重定向

# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        print("args[0]===%s" %args[0])
        self.regex = args[0]


# 2.Flask函数接收一个参数__name__，它会指向程序所在的包
app = Flask(__name__)

# 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: re
app.url_map.converters['re'] = RegexConverter


@app.route('/user/<re("[0-9]{3}"):user_id>')
# @app.route('/user/<int:user_id>')
def user_info(user_id):
    return 'hello %s' % user_id

# 3.装饰器的作用是将路由映射到视图函数 index
@app.route('/', methods=["GET", "POST"])
def index():
    return 'Hello World'

@app.route('/req', methods=["GET", "POST"])
def req():
    return request.args.get("a")


# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
@app.after_request
def after_request(response):
    print("after_request")
    response.headers["Content-Type"] = "application/json"
    return response


@app.errorhandler(500)  # (ZeroDivisionError) code_or_exception – HTTP的错误状态码或指定异常；abort(404)可以发异常
def internal_server_error(e):
    return '服务器搬家了'

# 返回JSON
@app.route('/demo3')
def demo3():
    json_dict = {
        "user_id": 10,
        "user_name": "laowang"
    }
    return jsonify(json_dict)


# 重定向
@app.route('/demo4')
def demo4():
    return redirect('http://www.baidu.com')
    # return redirect(url_for('demo3'))


if __name__ == '__main__':  # 4.Flask应用程序实例的 run 方法 启动 WEB 服务器
    app.run(debug=True)
