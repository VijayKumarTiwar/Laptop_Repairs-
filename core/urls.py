from django.urls import path
from .views import (
    HomeView, CityListView, BlogListView, ServicesView, AboutView, CitiesView, AppView,
    TermsView, PrivacyView, AntiDiscriminationView, RefundView, ContactView, PartnerView,
    BlogIndexView, BlogDetailView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('cities/', CitiesView.as_view(), name='cities'),
    path('app/', AppView.as_view(), name='app'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('anti-discrimination/', AntiDiscriminationView.as_view(), name='anti_discrimination'),
    path('refund/', RefundView.as_view(), name='refund'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('partner/', PartnerView.as_view(), name='partner'),
    path('blogs/', BlogIndexView.as_view(), name='blog_index'),
    path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('api/cities/', CityListView.as_view(), name='city-list'),
    path('api/blogs/', BlogListView.as_view(), name='blog-list'),
]
