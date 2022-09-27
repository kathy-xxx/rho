from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    #测试
    path('sample/', views.sample_view, name="sample_view"),
    path('sample2/', views.sample2_view, name="sample2_view"),
    path('sample3/', views.sample3_view, name="sample3_view"),
    path('data/dji/test/', views.get_test, name='test'),

    path('dji/', views.dji_view, name="dji_view"),
    path('dji/data/', views.get_dji_data, name='dji_data'),
]

urlpatterns += staticfiles_urlpatterns()
