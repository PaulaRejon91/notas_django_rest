from django.urls import path # This is the path function
from rest_framework import routers
from .api import NotesViewSet # This is the views file

router = routers.DefaultRouter()

router.register('api/notes', NotesViewSet, 'notes')

urlpatterns = router.urls