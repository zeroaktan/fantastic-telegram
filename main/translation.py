from modeltranslation.translator import register, TranslationOptions
from .models import Feedback, Faculty, University

@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ['user_info']

@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ['name']

@register(University)
class UniversityTranslationOptions(TranslationOptions):
    fields = ['uni_name']