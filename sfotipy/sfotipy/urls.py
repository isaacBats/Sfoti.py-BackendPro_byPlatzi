from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from artists.views import ArtistDetailView, ArtistListView
from artists.views import ArtistViewSet
from albums.views import AlbumViewSet
from tracks.views import TrackViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/password_rest/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_rest/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
    url(r'^artists/', ArtistListView.as_view()),
    url(r'^api/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

#if settings.DEBUG:
urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)