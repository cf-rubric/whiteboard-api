from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response

from .serializer import (
    InstructorSerialzer,
    StudentSerializer,
    ClassListSerializer,
    WhiteboardSerializer,
    WhiteboardImageSerializer,
    CategoryNotesSerializer,
    ScoreTableSerializer,
    )
from .models import (
    Instructors,
    Student, 
    ClassList,
    Whiteboard,
    WhiteboardImage,
    CategoryNotes,
    ScoreTable,
    )

# Create your views here.
class Overview(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class InstuctorAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = Instructors.objects.all()
    serializer_class = InstructorSerialzer

class ClassListAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = ClassList.objects.all()
    serializer_class = ClassListSerializer

class WhiteboardAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = Whiteboard.objects.all()
    serializer_class = WhiteboardSerializer


class WhiteboardImageAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = WhiteboardImage.objects.all()
    serializer_class = WhiteboardImageSerializer

class CategoryNotesAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = CategoryNotes.objects.all()
    serializer_class = CategoryNotesSerializer

class ScoreTableAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = IsAuthenticated
    queryset = ScoreTable.objects.all()
    serializer_class = ScoreTableSerializer


