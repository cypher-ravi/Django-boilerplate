from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()


urlpatterns = [
    # path('categories/',CategoryView.as_view()),
    
]+router.urls
