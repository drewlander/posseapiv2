from rest_framework import serializers

from .models import PosseQuote

class PosseQuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PosseQuote
        fields = ('quote', 'dateadded')