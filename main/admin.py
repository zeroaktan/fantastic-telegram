from django.contrib import admin
from .models import Feedback, Faculty
from modeltranslation.admin import TranslationAdmin

@admin.register(Feedback)
class FeedbackAdmin(TranslationAdmin):
    list_display = ['user_name']

@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}