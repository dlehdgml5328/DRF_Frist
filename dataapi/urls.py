from django.urls import path
from . import views

urlpatterns = [
    path("sample/", views.get_sample_data),
    path("test/", views.get_test_data),
]
