from wb_api_project.settings import ALLOWED_HOSTS
from django.urls import path
from django.contrib import admin
import environ 
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

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

urlpatterns = [ 
    path('', admin.site.urls),
    path('overview/',Overview.as_view()),
    # path('schedule-form/', SceduleFormView.as_view(), name='schedule-form'), #POST
   
]