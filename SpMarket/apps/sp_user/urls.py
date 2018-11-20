from django.conf.urls import url
from sp_user.views import (LoginView,
                           RegisterView,
                           ForgetPassView,
                           MemeberView,
                           InfomationView,
                           )

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),  # 登陆
    url(r'^register/$', RegisterView.as_view(), name="register"),  # 注册
    url(r'^forget/$', ForgetPassView.as_view(), name="forget"),  # 忘记密码
    url(r'^member/$', MemeberView.as_view(), name="member"),  # 个人中心
    url(r'^info/$', InfomationView.as_view(), name="info"),  # 个人资料
]
