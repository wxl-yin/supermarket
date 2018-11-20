"""SpMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include("sp_user.urls", namespace="sp_user")),  # 用户模块
    url(r'^goods/', include("sp_goods.urls", namespace="sp_goods")),  # 商品模块
    url(r'^cart/', include("sp_cart.urls", namespace="sp_cart")),  # 购物车模块
    url(r'^order/', include("sp_order.urls", namespace="sp_order")),  # 订单模块
]
