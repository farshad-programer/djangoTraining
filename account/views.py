from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import postSerializer

# Create your views here.


@api_view(["GET", "POST"])
def index(request):
    print(request.data)
    return Response(dict(request.data))


# -----------------به صورت داخلی -------------
# @api_view(["GET", "POST"])
# def index_post(request):
#     if request.method == "GET":
#         try:
#             p = Post.objects.get(pk=1)
#         except Post.DoesNotExist:
#             return Response(
#                 {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = postSerializer(p)
#         print(serializer)
#         return (Response(serializer.data))
#     else:
#         return Response(
#             {"detail": "there is no post"}, status=status.HTTP_400_BAD_REQUEST
#         )
# -----------------با استفاده از ادرس یو ار ال-------------
# @api_view(["GET", "POST"])
# def index_post(request,pk):
#     if request.method == "GET":
#         try:
#             p = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(
#                 {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
#             )


#         serializer = postSerializer(p)
#         print(serializer)
#         return (Response(serializer.data))
#     else:
#         return Response(
#             {"detail": "there is no post"}, status=status.HTTP_400_BAD_REQUEST
#         )
# -------------------------با استفاده از پارامتر-----------------------------
# @api_view(["GET", "POST"])
# def index_post(request):
#     if request.method == "GET":
#         pk = request.query_params.get("pk")
#         print("pk :", pk)
#         try:

#             p = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(
#                 {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = postSerializer(p)
#         print(serializer)
#         return Response(serializer.data)
#     else:
#         return Response(
#             {"detail": "there is no post"}, status=status.HTTP_400_BAD_REQUEST
#         )
# --------------------post and get data---------------------------
# @api_view(["GET", "POST"])
# def index_post(request):
#     if request.method == "POST":
#         pk = request.data.get("pk")
#         print("pk :", pk)
#         try:

#             p = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(
#                 {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = postSerializer(p)
#         print(serializer)
#         return Response(serializer.data)
#     else:
#         return Response(
#             {"detail": "there is no post"}, status=status.HTTP_400_BAD_REQUEST
#         )
# -------------------getClassBase--------------------
# from rest_framework.views import APIView


# class PostList(APIView):
#     def get(self, request):
#         try:
#             # posts = Post.objects.all()
#             posts = Post.objects.filter(title=1)
#             if not posts.exists():  # بررسی وجود پست‌ها
#                 return Response(
#                 {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
#             )
#         except Post.DoesNotExist:
#             return Response(
#                 {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = postSerializer(posts, many=True)
#         # data=postSerializer(posts,many=True).data
#         return Response(serializer.data)


# -------------------getClassBase--------------------
from rest_framework.views import APIView


class PostList(APIView):
    def get(self, request):
        try:
            pk = request.query_params.get("pk")
            posts = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(
                {"detail": "post not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        # serializer = postSerializer(posts, many=True)
        data = postSerializer(posts).data
        return Response(data)

    def post(self, request):
        serializer = postSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
