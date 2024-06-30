from django.urls import path

from .views import *


urlpatterns = [
    path('index/', index, name='index'),
    # path('post/', index_post, name='index_pos'),
    # path('post/<int:pk>/', index_post, name='index_pos'),
    # path('post/', index_post, name='index_pos'),
    # path('post/', PostList.as_view(), name='index_pos'),
    # path('post/<int:pk>/', PostList.as_view(), name='index_pos'), 
    path('post/', PostList.as_view(), name='index_pos'), 
]
