from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from test_api_apiview.models import AuthorApiView
from test_api_apiview.serializers import AuthorApiViewSerializer

# Create your views here.

class AuthorApiViews(APIView):

    def get(self, request, pk = None):
        if pk:
            author = AuthorApiView.objects.get(id = pk)
            serializers = AuthorApiViewSerializer(author)
        else:
            author = AuthorApiView.objects.all()
            serializers = AuthorApiViewSerializer(author, many=True)

        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers = AuthorApiViewSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = get_object_or_404(AuthorApiView, pk = pk)
        serializers = AuthorApiViewSerializer(author, data = request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = get_object_or_404(AuthorApiView, pk=pk)
        author.delete()
        return Response(status=status.HTTP_200_OK)

