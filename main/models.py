from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator

class University(models.Model):
    uni_name = models.CharField(max_length = 50, unique = True)
    uni_slug = models.SlugField(max_length = 50, unique = True)

    class Meta:
        ordering = ['uni_name']

    def get_absolute_url(self):
        return reverse('main:select_uni', args = [self.slug])
    
    def __str__(self):
        return self.uni_name


class Feedback(models.Model):
    user_name = models.CharField(max_length = 50)
    user_info = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'users_images/', blank = True)
    stars = models.PositiveIntegerField(blank = True, validators = [MaxValueValidator(5)], default = 5)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.user_name


class Faculty(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 50, unique = True)
    link = models.URLField()

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("main:select_by_faculty", args = [self.slug])

    def __str__(self):
        return self.name