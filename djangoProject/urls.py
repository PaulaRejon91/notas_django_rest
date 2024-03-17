from django.urls import path # path function
from . import views # views file

# Routes
urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/<str:pk>/', views.getNote, name='note')]