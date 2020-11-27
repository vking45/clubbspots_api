from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import UpdateView
from .models import Club, Report
from rest_framework import generics
from .serializers import clubsSerializer, reportSerializer


# Create your views here.
class ListClubs(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = clubsSerializer

class DetailClubs(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = clubsSerializer  

class UpdateClientView(UpdateView):
    queryset = Club.objects.all()
    model = Club
    template_name = 'update_cap.html'
    fields =  ['currcap']

class ListReports(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = reportSerializer



    