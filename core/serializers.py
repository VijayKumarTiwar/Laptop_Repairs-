from rest_framework import serializers
from .models import City, BlogPost, Service, Corporation, FAQ, Testimonial

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'state', 'is_active', 'image']

class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = ['id', 'name', 'logo_url', 'website', 'is_active']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'icon', 'order']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'order']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'location', 'content', 'rating', 'order']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'updated_at', 'excerpt', 'slug']
