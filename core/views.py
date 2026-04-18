from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, BlogPost
from .serializers import CitySerializer, BlogPostSerializer

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')

class CityListView(APIView):
    def get(self, request):
        cities = City.objects.filter(is_active=True)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

class BlogListView(APIView):
    def get(self, request):
        blogs = BlogPost.objects.all()[:6]
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)
