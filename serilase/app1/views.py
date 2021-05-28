from django.http import HttpResponse
from rest_framework.response import Response
# Create your views here.
from app1.models import car
from .serializers import carserializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

class carview(viewsets.ViewSet):

    def func(self, request):
        stu = car.objects.all()
        serializing = carserializer(stu, many=True)
        json_data = JSONRenderer().render(serializing.data)
        return HttpResponse(json_data)

    def func2(self, request):
        stu = car.objects.all()
        serializing = carserializer(stu, many=True)
        # json_data = JSONRenderer().render(serializing.data)
        return HttpResponse(serializing.data)

    def func3(self, request):
        try:
            name = request.data['name']
            model = request.data['model']
            number = request.data['number']
            x = car(name=name, model=model, number_plate=number)
            x.save()
            response = {
                'message': 'strER'
            }
            return Response(response)


        except Exception as EOFError:
            response = {
                'message': str(EOFError)
            }
            return Response(response)

    def delete_details(self, request, pk):
        model = car.objects.get(id=pk)
        model.delete()
        response = {
            'message': 'deleted'}
        return Response(response)

    def overwrite_details(self, request, num):
        name = request.data['name']
        model = request.data['model']
        number = request.data['number']
        model_data = car.objects.filter(id=num).values()
        model_data.update(name=name, model=model, number_plate=number)
        # serializing = carserializer(model_data)
        response = {
            'message': 'updated'}
        return Response(response)
        # return Response(serializing.data)

    def partial_update(self, request, num):
        name = request.data['name']
        model = request.data['model']
        number = request.data['number']
        model_data = car.objects.filter(id=num).values()
        model_data.update(name=name, model=model, number_plate=number)
        # serializing = carserializer(model_data)
        response = {
            'message': 'updated'}
        return Response(response)
        # return Response(serializing.data)
