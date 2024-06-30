from rest_framework import permissions, viewsets ,status

from .models import Post
from .serializers import postSerializer

# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = postSerializer
    
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
