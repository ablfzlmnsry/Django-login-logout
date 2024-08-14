from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
from basic_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path('admin/', admin.site.urls),
    re_path(r'^basic_app/', include('basic_app.urls')),
    re_path(r'^logout/$', views.user_logout, name="logout"),
    re_path(r'^special/', views.special, name='special'),
]
