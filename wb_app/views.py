from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
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
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class InstuctorAPIView(generics.ListAPIView):
    queryset = Instructors.objects.all()
    serializer_class = InstructorSerialzer


class ClassListAPIView(generics.ListAPIView):
    queryset = ClassList.objects.all()
    serializer_class = ClassListSerializer


class WhiteboardAPIView(generics.ListAPIView):
    queryset = Whiteboard.objects.all()
    serializer_class = WhiteboardSerializer



class WhiteboardImageAPIView(generics.ListAPIView):
    queryset = WhiteboardImage.objects.all()
    serializer_class = WhiteboardImageSerializer


class CategoryNotesAPIView(generics.ListAPIView):
    queryset = CategoryNotes.objects.all()
    serializer_class = CategoryNotesSerializer


class ScoreTableAPIView(generics.ListAPIView):
    queryset = ScoreTable.objects.all()
    serializer_class = ScoreTableSerializer


# class ScheduleStudentAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = [
#         Whiteboard.objects.all(), 
#         WhiteboardImage.objects.all(),
#         ScoreTable.objects.all(),
#         CategoryNotes.objects.all(),
#         ]


# class ScheduleAPIView(generics.ListAPIView):
#     pass  


