from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import car_model, engine_model,employee1,department1
from .seralizers import engine_serializer, car_serializer, employee1_serializer,department1_serialzer

from rest_framework.response import Response


class func1(ModelViewSet):
    queryset = car_model.objects.all()
    serializer_class = car_serializer

    def create(self, request):
        model__ = engine_model.objects.create(
            cc=request.data["_new"]["cc"],
            color=request.data["_new"]["color"],
        )
        model__.save()
        model_ = car_model.objects.create(
            name=request.data["name"],
            model_no=request.data["model_no"],
            _new=model__,
        )
        model_.save()
        response = {
            'message': 'created'
        }
        return Response(response)


# class second_view(ModelViewSet):
#     queryset = d_epartment.objects.all()
#     serializer_class = department_serialzer
#
#     def create(self, request):
#         model__ = e_mployee.objects.create(
#             name=request.data["_info"]["name"],
#             age=request.data["_info"]["age"],
#         )
#         model__.save()
#         model_ = d_epartment.objects.create(
#             name=request.data["name"],
#             location=request.data["location"],
#             _info=model__
#         )
#         model_.save()
#         serializing = department_serialzer(model_)
#         return Response(serializing.data)


class third_view(ModelViewSet):
    queryset = department1.objects.all()
    serializer_class = department1_serialzer

    def create(self, request):
        model__ = employee1.objects.create(
            name=request.data["_info"]["name"],
            age=request.data["_info"]["age"],
        )
        model__.save()
        model_ = department1.objects.create(
            name=request.data["name"],
            location=request.data["location"],
            _info=model__
        )
        model_.save()
        serializing = department1_serialzer(model_)
        return Response(serializing.data)
