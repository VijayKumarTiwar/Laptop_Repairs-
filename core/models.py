from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    updated_at = models.DateField()
    excerpt = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
