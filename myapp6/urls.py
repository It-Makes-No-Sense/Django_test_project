from django.urls import path
from .views import total_in_view, total_in_db, total_in_template

urlpatterns = [
    path('view/', total_in_view, name='view'),
    path('db/', total_in_db, name='db'),
    path('template/', total_in_template, name='template'),
]
