from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, BlogPost, Service, FAQ, Testimonial
from .serializers import CitySerializer, BlogPostSerializer, ServiceSerializer, FAQSerializer, TestimonialSerializer

class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')

class ServicesView(View):
    def get(self, request):
        return render(request, 'core/services.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'core/about.html')

class CitiesView(View):
    def get(self, request):
        return render(request, 'core/cities.html')

class AppView(View):
    def get(self, request):
        return render(request, 'core/app.html')

class TermsView(View):
    def get(self, request):
        return render(request, 'core/terms.html')

class PrivacyView(View):
    def get(self, request):
        return render(request, 'core/privacy.html')

class AntiDiscriminationView(View):
    def get(self, request):
        return render(request, 'core/anti_discrimination.html')

class RefundView(View):
    def get(self, request):
        return render(request, 'core/refund.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'core/contact.html')

class PartnerView(View):
    def get(self, request):
        return render(request, 'core/partner.html')

class BlogIndexView(View):
    def get(self, request):
        blogs = BlogPost.objects.all().order_by('-updated_at')
        return render(request, 'core/blog_index.html', {'blogs': blogs})

class BlogDetailView(View):
    def get(self, request, slug):
        blog = get_object_or_404(BlogPost, slug=slug)
        return render(request, 'core/blog_detail.html', {'blog': blog})

class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.filter(is_active=True)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class FAQListView(APIView):
    def get(self, request):
        faqs = FAQ.objects.filter(is_active=True)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

class TestimonialListView(APIView):
    def get(self, request):
        testimonials = Testimonial.objects.filter(is_active=True)
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

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
