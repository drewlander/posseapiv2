from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PosseQuoteSerializer
from .models import PosseQuote


class PosseQuoteViewSet(viewsets.ModelViewSet):
    queryset = PosseQuote.objects.all().order_by('quote')
    serializer_class = PosseQuoteSerializer
