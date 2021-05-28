from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import student
from .serializee import student_serializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


# Create your views here.

class student_view(ModelViewSet):
    serializer_class = student_serializer
    queryset = student.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def delete_(self, request, **kwargs):
        id = kwargs['id']
        model_ = student.objects.filter(id=id)
        model_.delete()
        response = {
            'message': 'deleted'
        }
        return Response(response)

    def create_(self, request):
        name = request.data['name']
        roll_number = request.data['roll_number']
        section = request.data['section']
        model_ = student(name=name, roll_number=roll_number, section=section)
        model_.save()
        response = {
            'message': 'user created'
        }
        return Response(response)


class viewstudent(ModelViewSet):
    serializer_class = student_serializer
    queryset = student.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete_(self, request, **kwargs):
        id = kwargs['id']
        model_ = student.objects.filter(id=id)
        model_.delete()
        response = {
            'message': 'deleted'
        }
        return Response(response)

    def create_(self, request):
        name = request.data['name']
        roll_number = request.data['roll_number']
        section = request.data['section']
        model_ = student(name=name, roll_number=roll_number, section=section)
        model_.save()
        response = {
            'message': 'user created'
        }
        return Response(response)

