from django.urls import path, include
from rest_framework import routers

from directory_app.views import DirectoryViewSet,EstablishmentsByCategory,DirectoryListViewSet,EstablishmentsByCity

router = routers.DefaultRouter()
router.register("directoryinfo", DirectoryViewSet, "directoryinfo")  
router.register("directorylist", DirectoryListViewSet, "directorylist")  


urlpatterns = [
    path('', include(router.urls)),

    path('directory/category/<int:category_id>', EstablishmentsByCategory.as_view()),
    path('directory/city/<int:city_id>', EstablishmentsByCity.as_view()),
]