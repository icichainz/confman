from rest_framework import serializers
from .models import Project, Environment, SecretVersion

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'

class SecretVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretVersion
        fields = '__all__'
