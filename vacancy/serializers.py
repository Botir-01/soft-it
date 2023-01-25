from rest_framework import serializers
from .models import Vacancy, VacanyRequirement, VacanyTask, VacanyCondition, UserResume

class VacancyRequirementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'content'
        ]
        model = VacanyRequirement

class VacanyTaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'content'
        ]
        model = VacanyTask

class VacanyConditionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'content'
        ]
        model = VacanyCondition

class VacancyListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title', 'working_days', 'working_hours', 'salary'
        ]
        model = Vacancy

class AvailableVacancyList(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title'
        ]
        model = Vacancy

class VacancyDetailSerializer(serializers.ModelSerializer):
    requirements = VacancyRequirementSerializer(many=True, read_only=True)
    tasks = VacanyTaskSerializer(many=True, read_only=True)
    conditions = VacanyConditionSerializer(many=True, read_only=True)

    class Meta:
        fields = [
            'id', 'title', 'working_days', 'working_hours', 'salary', 'requirements', 'tasks', 'conditions'
        ]
        model = Vacancy


class UserResumeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'full_name', 'phone_number', 'vacancy_id', 'cv_file'
        ]
        model = UserResume