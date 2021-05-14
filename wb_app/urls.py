from wb_api_project.settings import ALLOWED_HOSTS
from django.urls import path
from django.contrib import admin

from .views import (
    Overview,
    InstuctorAPIView,
    ClassListAPIView,
    WhiteboardAPIView,
    WhiteboardAPIView,
    WhiteboardImageAPIView,
    CategoryNotesAPIView,
    ScoreTableAPIView,
    # SceduleFormView,
    )



urlpatterns = [ 
    path('', Overview.as_view()), # only hit as a result of authentication front-end
    # status response 'ok' (handled by JWT between React and Django.)

    
    # TODO: below path necesary for scheduling functionality. (now a stretch-goal)
    # path('schedule-form/', SceduleFormView.as_view(), name='schedule-form'), #POST

]