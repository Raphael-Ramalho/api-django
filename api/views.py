from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# View is an class (or function) that receives an HTTP request, process data and returns a response


class BlogPostListCreate(generics.ListCreateAPIView): # abstraction to list view
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): # abstraction to update or destroy view
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk" # pk = primary key

class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")
        
        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()
            
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)