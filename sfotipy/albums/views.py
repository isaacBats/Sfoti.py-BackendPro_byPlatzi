from django.shortcuts import render

# Create your views here.
from .models import Album
from rest_framework import viewsets
from .serializers import AlbumSerializer

class AlbumViewSet(viewsets.ModelViewSet):
	# model = Album
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer