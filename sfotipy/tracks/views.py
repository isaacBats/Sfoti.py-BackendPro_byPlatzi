import json
import time

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Track
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from artists.tasks import demorada

# Create your views here.
# @cache_page(60)
@login_required
def track_view(request, title):
	#import ipdb; ipdb.set_trace()	
	# try:
	# 	track = Track.objects.get(title=title)
	# except Track.DoesNotExist:
	# 	raise Http404

	#La siguiente linea pasa a sistituir el try de arriba ya que es un 
	#shortcut de django para 404
	track = get_object_or_404(Track, title=title)
	bio = track.artist.biography
	data = cache.get('data_%s' % title)
	if data is None:
		data = {
			'title': track.title,
			'order': track.order,
			'album': track.album.title,
			'artist': {
				'name':track.artist.first_name,
				'bio': bio,
		}
	}
	demorada.apply_async(countdown=5)
	# time.sleep(5)
	cache.set('data_%s' % title, data)

	return render(request, 'track.html', {'track':track, 'bio':bio})
	#return HttpResponse('Ok')
	
	#con la siguiente instruccion convertimos el diccionario de python a json
	#json_data = json.dumps(data)
	#return HttpResponse(json_data, content_type='application/json')

	#Tarea: como podemos serializar todo el track junto con el album y el artista
	#revisar serialization django.

from rest_framework import viewsets
from .serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
    # model = Track
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    