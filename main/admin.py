from django.contrib import admin
from .models import Feedback, Faculty, University
from modeltranslation.admin import TranslationAdmin

@admin.register(Feedback)
class FeedbackAdmin(TranslationAdmin):
    list_display = ['user_name']

@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    list_display = ['uni_name', 'uni_slug']
    prepopulated_fields = {'uni_slug': ('uni_name', )}