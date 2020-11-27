from rest_framework import serializers
from .models import Club, Report

class clubsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'

class reportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'