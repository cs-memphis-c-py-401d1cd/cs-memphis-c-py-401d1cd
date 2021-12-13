from rest_framework import generics
from .serializers import PostSerializer
from .models import Posts
# Extra for future processing examples
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# class PostList(generics.ListAPIView): # Original method signature FOR LIST/READ+1
class PostList(generics.ListCreateAPIView):  # This dignature handles list AND create      
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# The postDetail needs the same things
# class PostDetail(generics.RetrieveAPIView): # Original signature for READ
# class PostDetail(generics.RetrieveUpdateAPIView): # Original signature for READ one and UPDATE
class PostDetail(generics.RetrieveUpdateDestroyAPIView): # This signature handles READ/UPDATE/DELETE one
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
