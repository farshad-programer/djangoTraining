from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"", PostView, basename="posts")
urlpatterns = [
    # path('post/', PostView.as_view({'get':'list','post':'create'}), name='postView'),
    # path('post/<int:pk>/', PostView.as_view({'get':'retrieve','post':'update','delete':'destroy'}), name='postView'),
    path("post/", include(router.urls)),
]
