from django.http import Http404
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .models import Post
from .serializers import postSerializer

# Create your views here.


class PostListView(
    generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class = postSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# CRUD --create , retrieve ,
class PostDetailView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Post.objects.all()
    serializer_class = postSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
