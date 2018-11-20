from django.shortcuts import render
from django.views import View

"""
    开始定义视图:
    1. 函数
    2. 视图类
        a. 定义一个类, 继承 View
        b. 定义方法, 方法名一定要和请求方式名同名(小写 get,post)
        c. 所有的方法都第一个参数和第二个都是固定: self,request
"""


class LoginView(View):
    """登陆"""

    def get(self, request):
        pass

    def post(self, request):
        pass


class RegisterView(View):
    """注册"""

    def get(self, request):
        pass

    def post(self, request):
        pass


class ForgetPassView(View):
    """找回密码"""

    def get(self, request):
        pass

    def post(self, request):
        pass


class MemeberView(View):
    """个人中心"""

    def get(self, request):
        pass

    def post(self, request):
        pass


class InfomationView(View):
    """个人资料"""

    def get(self, request):
        pass

    def post(self, request):
        pass
