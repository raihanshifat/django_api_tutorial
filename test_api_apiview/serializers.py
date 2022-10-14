from rest_framework import serializers
from test_api_apiview.models import AuthorApiView

class AuthorApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorApiView
        fields = "__all__"
