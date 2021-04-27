from rest_framework import serializers
from .models import *
from user.serializers import ProfileSerializer


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer()
    language = LanguageSerializer()
    programming_languages = ProgrammingLanguagesSerializer()

    class Meta:
        model = Courses
        fields = '__all__'
