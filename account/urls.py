from django.urls import path

from .views import *


urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='bvv'), 
    path('post/', PostListView.as_view(), name='index_pos'), 
]
