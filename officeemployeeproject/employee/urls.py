from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('emplist/', views.list_view, name='list'),
    path('add_emp/', views.add_view, name='add_emp'),
    path('remove_emp/', views.remove_view, name='remove_emp'),
    path('remove_emp/<int:id>', views.remove_view),
    path('filter/', views.filter_view, name='filter'),

    
]
