from django.shortcuts import render

from rest_framework import generics
from .serializers import VisitorSerializer
from .models import Visitor

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api"""
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new visitor"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer