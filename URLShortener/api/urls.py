from django.conf.urls import include,url
from django.urls import path,include,re_path
from rest_framework import renderers
from api import views


urlpatterns = [
        #path('create?url=<slug:url>',ShortUrlViewSet.as_view({'put':'create','get':'create'})),

        re_path(r'create?.+$',views.ShortUrlViewSet.as_view({'put':'create','get':'create'})),
        path('list',views.ShortUrlViewSet.as_view({'get':'list'})),
        path('<slug:pk>',views.ShortUrlViewSet.as_view({'get':'retrieve'})),
        path('',views.index,name='index')
    ]