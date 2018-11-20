from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from sp_user.forms import RegisterModelForm
from sp_user.helper import set_password
from sp_user.models import SpUser

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
        return render(request, "sp_user/login.html")

    def post(self, request):
        pass


class RegisterView(View):
    """注册"""

    def get(self, request):
        return render(request, "sp_user/reg.html")

    def post(self, request):
        # 处理
        # 1. 接收
        data = request.POST
        # 2. 处理
        # 验证是否合法
        form = RegisterModelForm(data)
        if form.is_valid():
            # 处理,保存到数据库
            data = form.cleaned_data
            # 密码需要加密
            password = data.get('password2')
            password = set_password(password)
            # 保存到数据库
            SpUser.objects.create(phone=data.get('phone'), password=password)

            # 成功跳转到登陆页面
            return redirect("sp_user:login")
        else:
            # 传递错误信息到页面
            context = {
                "errors": form.errors,
            }
            # 3. 响应
            return render(request, "sp_user/reg.html", context)


class ForgetPassView(View):
    """找回密码"""

    def get(self, request):
        return render(request, "sp_user/forgetpassword.html")

    def post(self, request):
        pass


class MemeberView(View):
    """个人中心"""

    def get(self, request):
        return render(request, 'sp_user/member.html')

    def post(self, request):
        pass


class InfomationView(View):
    """个人资料"""

    def get(self, request):
        return render(request, 'sp_user/infor.html')

    def post(self, request):
        pass
