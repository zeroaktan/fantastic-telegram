from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main_land, name = 'main_land'),
    path('university/', views.product_list, name = 'product_list'),
    path('university/<slug:slug>/', views.product_detail, name = 'product_detail'),
    path('university/category/<slug:category_slug>', views.product_list, name = 'product_list_by_category'),
]