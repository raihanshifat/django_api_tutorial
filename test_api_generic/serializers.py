from rest_framework import serializers
from test_api_generic.models import AuthorGeneric, AuthorGenericv2, AuthorGenericv3

class AuthorGenericSerializerv1(serializers.ModelSerializer):
    class Meta:
        model = AuthorGeneric
        fields = "__all__"

class AuthorGenericSerializerv2(serializers.ModelSerializer):
    class Meta:
        model = AuthorGenericv2
        fields = "__all__"

class AuthorGenericSerializerv3(serializers.ModelSerializer):
    class Meta:
        model = AuthorGenericv3
        fields = "__all__"