from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import postSerializer

# Create your views here.


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = postSerializer(instance=posts, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = postSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CRUD --create , retrieve ,
class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            posts = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(
                {"detail": "there is no post"}, status=status.HTTP_404_NOT_FOUND
            )

        # serializer = postSerializer(posts, many=True)
        data = postSerializer(posts).data
        return Response(data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = postSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
