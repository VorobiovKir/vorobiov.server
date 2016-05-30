from rest_framework import generics, viewsets

from .serializers import LanguageSerializer
from .models import Language


class LanguagesList(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
