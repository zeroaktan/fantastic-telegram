from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_land, name = 'main_land'),
    path('faculty/', views.selection, name = 'selection'),
    path('faculty/<slug:slug>', views.selected, name = 'selected'),
    path('added/', views.selected, name = 'added'),
]