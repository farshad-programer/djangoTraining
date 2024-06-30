from rest_framework import generics

from .models import Post
from .serializers import postSerializer

# Create your views here.


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer


# CRUD --create , retrieve ,
class PostDetailView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Post.objects.all()
    serializer_class = postSerializer
