from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard, name = 'dashboard'),
    url(r'^wish_items/(?P<id>\d+)$', views.item, name = 'item'),
    url(r'^add$', views.add, name= 'add'),
    url(r'^wish_items/create$', views.create, name= 'create'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
    url(r'^createById/(?P<id>\d+)$', views.createById, name = 'createById'),
    url(r'^remove/$', views.remove, name = 'remove')
]
