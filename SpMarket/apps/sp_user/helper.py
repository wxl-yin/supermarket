import hashlib
from django.conf import settings
from django.shortcuts import redirect


def set_password(password):
    # 加密方法
    # 新的加密字符串
    new_password = "{}{}".format(password, settings.SECRET_KEY)
    h = hashlib.md5(new_password.encode('utf-8'))
    return h.hexdigest()


def login(request, user):
    # 登陆保存session的方法
    # 将用户id和手机号码,保存到session中
    request.session['ID'] = user.pk
    request.session['phone'] = user.phone
    # request.session['head'] = user.head



def verify_login(func):
    """验证登陆装饰器"""
    def check_loign(request, *args, **kwargs):
        if request.session.get("ID") is None:
            return redirect('sp_user:login')
        else:
            return func(request, *args, **kwargs)
    return check_loign
