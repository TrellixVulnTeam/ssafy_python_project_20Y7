from django.urls import path
from . import views

urlpatterns = [
    # 화면 추가 path("경로", 해당 경로)
    path('index/', views.index, name="index"),
    path('greeting/', views.greeting, name="greeting"),
    path('dinner/', views.dinner, name="dinner"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('hello/<name>&<age>/', views.hello, name="hello")
]