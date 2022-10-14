from django.urls import path
from test_api_apiview.views import AuthorApiViews

urlpatterns = [
    path("author_api_view/",AuthorApiViews.as_view()),
    path("author_api_view/<str:pk>",AuthorApiViews.as_view()),
]