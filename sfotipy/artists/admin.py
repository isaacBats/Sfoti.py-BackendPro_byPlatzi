from django.contrib import admin
from .models import Artist
from tracks.models import Track
from albums.models import Album
# Register your models here.

class TrackInLine(admin.StackedInline):
	model = Track
	extra = 1

class AlbumInline (admin.StackedInline):
	model = Album
	extra = 1

class ArtistAdmin(admin.ModelAdmin):
	search_fields = ('first_name', 'last_name',)
	#filter_horizontal = ('favorite_songs',)
	filter_vertical = ('favorite_songs',)
	inlines = [AlbumInline, TrackInLine]


admin.site.register(Artist, ArtistAdmin)

