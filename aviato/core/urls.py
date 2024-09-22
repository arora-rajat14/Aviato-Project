from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CandidateViewSet

# Create a router and register the CandidateViewSet with it
router = DefaultRouter()
router.register(r"candidates", CandidateViewSet, basename="candidate")

# Include the router's generated URLs
urlpatterns = [
    path("", include(router.urls)),
]
