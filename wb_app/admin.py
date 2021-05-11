from django.contrib import admin
from .models import (
    Instructors,
    Student, 
    ClassList,
    Whiteboard,
    WhiteboardImage,
    CategoryNotes,
    ScoreTable,
    )
# Register your models here.
admin.site.register(Instructors)
admin.site.register(Student)
admin.site.register(ClassList)
admin.site.register(Whiteboard)
admin.site.register(WhiteboardImage)
admin.site.register(CategoryNotes)
admin.site.register(ScoreTable)