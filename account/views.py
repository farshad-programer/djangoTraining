from rest_framework import viewsets

from .models import Post
from .serializers import postSerializer

# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = postSerializer

