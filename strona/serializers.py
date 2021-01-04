from rest_framework import serializers
from .models import movie

class movieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = movie
        fields = ('title', 'image', 'description', 'rate', 'ticketPrice', 'ticketAvailability', )

