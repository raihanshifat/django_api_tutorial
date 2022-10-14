from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from test_api.models import Author
from test_api.serializers import AuthorSerializer

# Create your views here.
class ApiTutorialViewset(viewsets.ViewSet):

    queryset = Author.objects.all()

    def list(self, request):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def update(self, request, pk):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        author = get_object_or_404(self.queryset, pk=pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        author = get_object_or_404(self.queryset, pk=pk)
        author.delete()
        return Response(status=status.HTTP_200_OK)




