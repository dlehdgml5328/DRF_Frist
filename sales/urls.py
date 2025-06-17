from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("sales/monthly/", views.monthly_sales_summary),
    path("sales/category/", views.category_sales_summary),
]

urlpatterns = format_suffix_patterns(urlpatterns)
