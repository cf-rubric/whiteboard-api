from django.urls import path
from .views import (
    Overview,
    InstuctorAPIView,
    ClassListAPIView,
    WhiteboardAPIView,
    WhiteboardAPIView,
    WhiteboardImageAPIView,
    CategoryNotesAPIView,
    ScoreTableAPIView,
    )

urlpatterns = [ 
    path('', Overview.as_view())

]