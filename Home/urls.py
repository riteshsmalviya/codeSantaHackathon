from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path("",views.index, name='Home'),
    path("code",views.code,name="code"),
    path("share",views.share,name="share"),
    path("needcode",views.needcode,name="needcode"),
    path("c",views.c,name="c"),
    path("cpp",views.cpp,name="cpp"),
    path("java",views.java,name="java"),
    path("python",views.python,name="python"),
    path("js",views.js,name="js"),
    path("sql",views.sql,name="sql"),
    
    
]