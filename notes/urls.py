from django.urls import include, path # This is the path function
from rest_framework import routers
from .viewset import NotesViewSet # This is the views file

router = routers.DefaultRouter()
router.register(r'notes', NotesViewSet, basename='note')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]