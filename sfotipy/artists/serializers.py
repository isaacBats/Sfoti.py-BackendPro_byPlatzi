from rest_framework import serializers

from .models import Artist

#class ArtistSerializer(serializers.HyperlinkedModelSerializer):
class ArtistSerializer(serializers.ModelSerializer):
    es_pharrel_1 = serializers.SerializerMethodField('es_pharrel_2')

    def es_pharrel_2(self, obj):
        return obj.es_pharrel()

    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'es_pharrel_1')