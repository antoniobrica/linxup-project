from django.urls import path
from . import views

urlpatterns = [
    path('register/page1/', views.register_page1, name='register_page1'),
    path('register/page2/', views.register_page2, name='register_page2'),
]
