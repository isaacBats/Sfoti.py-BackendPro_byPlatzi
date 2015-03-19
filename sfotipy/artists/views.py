from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'fav_artist'
	template_name = 'artist.html'

	# def get_template_names(self):
	# 	return 'artist.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artist'
	template_name = 'artist.html'

from rest_framework import viewsets
# from .serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    model = Artist
#     serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    # filter_fields = ('id', 'first_name','last_name', )
    # paginate_by = 1
    
#from django.contrib.auth.models import User, Group