from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 50, unique = True, default='temp')
    slug = models.SlugField(max_length = 50, unique = True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields = ['name'])]
        verbose_name = 'university'
        verbose_name_plural = 'universities'

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args = [self.slug])
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique = True)
    link = models.URLField()

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields = ['slug']),
            models.Index(fields = ['name']),
        ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:product_detail', args = [self.slug])