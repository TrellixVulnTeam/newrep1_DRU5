from django.shortcuts import render

# Create your views here.
import rest_framework.viewsets
from .models import department_model, employee_model, student, projects
from .serializer import department1_serialzer, employee1_serializer, student_serializer, project_serializer
from rest_framework.response import Response
from elasticsearch import Elasticsearch


class func(ModelViewSet):
    queryset = department_model.objects.all()
    serializer_class = department1_serialzer

    def create(self, request, *args, **kwargs):
        if request.data is not None:
            location = request.data['location']
            nameadd = request.data['name']
            added_info = request.data['_info']
            info = employee_model.objects.get(id=added_info)
            department_model.objects.create(
                name=nameadd,
                location=location,
                _info=info
            )
        response = {
            'message': 'created'
        }
        return Response(response)

    # def up(self, request, id):
    #     if request.data is not None:
    #         model_ = department_model.objects.filter(id=id)
    #         location = request.data['location']
    #         nameadd = request.data['name']
    #         added_info = request.data['_info']
    #         model_.update(name=nameadd, location=location)
    #         model = employee_model.objects.filter(id=added_info)
    #         employee_name = request.data['name']
    #         employee_age = request.data['age']
    #         model.update(name=employee_name,age=employee_age)
    #         model.update()
    #
    #     response = {
    #         'message': 'updated'
    #     }
    #     return Response(response)


#
class project_class(ModelViewSet):
    serializer_class = project_serializer
    queryset = projects.objects.all()

    def create(self, request, *args, **kwargs):
        project_name = projects.objects.create(project_name=request.data['project_name'])
        project_name.save()
        for i in request.data['_info']:
            info = student.objects.get(name=i['name'])
            project_name._info.add(info)
        response = {
            'message': 'created'
        }
        return Response(response)


class student_class(ModelViewSet):
    serializer_class = student_serializer
    queryset = student.objects.all()
