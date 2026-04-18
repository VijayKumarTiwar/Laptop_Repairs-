from django.urls import path
from .views import HomeView, CityListView, BlogListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/cities/', CityListView.as_view(), name='city-list'),
    path('api/blogs/', BlogListView.as_view(), name='blog-list'),
]
