from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from test_api_generic.models import (
    AuthorGeneric,
    AuthorGenericv2,
    AuthorGenericv3
)
from test_api_generic.serializers import (
    AuthorGenericSerializerv1,
    AuthorGenericSerializerv2,
    AuthorGenericSerializerv3
)

# Create your views here.
class generic_views_v1(
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = AuthorGeneric.objects.all()
    serializer_class = AuthorGenericSerializerv1

    def get(self, request, pk = None):
        if not pk:
            return self.list(request)
        else:
            return self.retrieve(request, pk)

    def post(self,request):
        return self.create(request)

    def put(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class generic_views_v2(
    generics.CreateAPIView,
    generics.ListAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.RetrieveAPIView,
):
    queryset = AuthorGenericv2.objects.all()
    serializer_class = AuthorGenericSerializerv2

class generic_views_v3(ModelViewSet):
    queryset = AuthorGenericv3.objects.all()
    serializer_class = AuthorGenericSerializerv3

