from django.contrib import admin
from .models import City, BlogPost

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
