from django.urls import path, include
from rest_framework import routers
from test_api.views import ApiTutorialViewset

author_router = routers.DefaultRouter()
author_router.register(r'author', ApiTutorialViewset)

urlpatterns = [
    path("", include(author_router.urls))
]