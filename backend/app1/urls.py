from django.urls import path, include
from .views import ModelNameList

urlpatterns = [
    path('modelname/', ModelNameList.as_view()),  # Endpunkt für die List- und Create-Methoden
    path('api/', include('app1.urls')),
]
