from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.generics import ListAPIView

from directory_app.models import Establishments,Category
from directory_app.serializers import EstablishmentsSerializer,EstablishmentsListSerializer

class DirectoryViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsSerializer

class DirectoryListViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsListSerializer

 
class EstablishmentsByCategory(ListAPIView):
    serializer_class = EstablishmentsSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Establishments.objects.filter(category_id=category_id)
        return queryset

class EstablishmentsByCity(ListAPIView):
    serializer_class = EstablishmentsSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        queryset = Establishments.objects.filter(city_id=city_id)
        return queryset

        