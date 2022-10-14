from django.urls import path, include
from rest_framework import routers

from test_api_generic.views import generic_views_v1, generic_views_v2, generic_views_v3

viewset_router = routers.DefaultRouter()
viewset_router.register("modelviewset",generic_views_v3)

urlpatterns = [
    path("autour_generic_v1/",generic_views_v1.as_view()),
    path("autour_generic_v1/<str:pk>",generic_views_v1.as_view()),
    path("autour_generic_v2/", generic_views_v2.as_view()),
    path("autour_generic_v2/<str:pk>", generic_views_v2.as_view()),
    path("",include(viewset_router.urls))
]