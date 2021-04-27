from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializer


class CoursesListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
