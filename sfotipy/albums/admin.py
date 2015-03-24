from django.contrib import admin

from .models import Album
from sorl.thumbnail import get_thumbnail
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'imagen_album')

	def imagen_album(self, obj):
		# return '<img src="%s">' % get_thumbnail(obj.cover, '50x500', crop='center', format='PNG').url
		return '<img src="%s">' % get_thumbnail(obj.cover, '50x50', format='PNG').url
	imagen_album.allow_tags = True

admin.site.register(Album, AlbumAdmin)