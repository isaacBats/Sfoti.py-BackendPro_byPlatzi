import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
# Create your views here.
#@login_required
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
	
	#return HttpResponse('Ok')
	return render(request, 'track.html', {'track':track, 'bio':bio})

	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name':track.artist.first_name,
			'bio': bio,
		}
	}

	#con la siguiente instruccion convertimos el diccionario de python a json
	#json_data = json.dumps(data)

	#return HttpResponse(json_data, content_type='application/json')



	#Tarea: como podemos serializar todo el track junto con el album y el artista
	#revisar serialization django.