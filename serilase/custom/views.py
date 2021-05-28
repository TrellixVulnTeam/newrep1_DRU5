from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import employee1
from .serializer import employee12_serializer
from rest_framework.response import Response
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView

class four(APIView):
    def get(self, request):
        if request.user.has_permission('custom.can_add_employee1'):
            return Response('hello')