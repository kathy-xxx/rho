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

    path('ixic/', views.ixic_view, name="ixic_view"),
    path('ixic/data/', views.get_ixic_data, name='ixic_data'),

    path('ndx/', views.ndx_view, name="ndx_view"),
    path('ndx/data/', views.get_ndx_data, name='ndx_data'),

    path('ndx-future/', views.ndx_future_view, name="ndx_future_view"),
    path('ndx-future/data/', views.get_ndx_future_data, name='ndx_future_data'),
]

urlpatterns += staticfiles_urlpatterns()
