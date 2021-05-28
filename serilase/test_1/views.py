from django.shortcuts import render

# Create your views here.
from . import elastic
from .elastic import search
import datetime
from rest_framework import status
from .models import student_model, projects, blood_model, subjects, company, employee_model, assing
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .seria import proj_serializer, blood_serializer, subject_serializer, company_serializer, employee_serializer, \
    assing_serializer

ess_object = elastic.search()


class func_viewset(ModelViewSet):
    queryset = projects.objects.all()
    serializer_class = proj_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        proj_name = request.data['proj_name']
        x = request.data['info']
        info = student_model.objects.get(id=x)
        result = projects.objects.create(
            proj_name=proj_name,
            info=info
        )
        response = {
            'message': 'created'
        }
        return Response(response)


class func2_view(ModelViewSet):
    queryset = blood_model.objects.all()
    serializer_class = blood_serializer

    def create(self, request):
        blood_group = request.data['blood_group']
        dep_info = request.data['dep_info']
        x = student_model.objects.get(id=dep_info)
        result = blood_model.objects.create(
            blood_group=blood_group,
            dep_info=x,
        )
        response = {
            'message': 'created'
        }
        return Response(response)


class func3_veiw(ModelViewSet):
    queryset = subjects.objects.all()
    serializer_class = subject_serializer

    def create(self, request):
        subject_name = request.data['subject_name']
        subject_info = request.data['subject_info']
        x = student_model.objects.get(id=subject_info)
        result = subjects.objects.create(
            subject_name=subject_name,
            subject_info=x,
        )
        response = {
            'message': 'created'
        }
        return Response(response)


class func4_veiw(ModelViewSet):
    queryset = employee_model.objects.all()
    serializer_class = employee_serializer

    def create(self, request):
        model2 = company.objects.create(
            company_name=request.data['company_info']['company_name'],
        )
        model2.save()
        model1 = employee_model.objects.create(
            emp_name=request.data['emp_info']['emp_name'],
            emp_reg=request.data['emp_info']['emp_reg'],
            company_info=model2

        )
        model1.save()

        response = {
            'message': 'created'
        }
        return Response(response)


class func5_veiw(ModelViewSet):
    queryset = assing.objects.all()
    serializer_class = assing_serializer

    def create(self, request):
        assing_name = request.data['assing_name']
        model = assing.objects.create(
            assing_name=assing_name
        )
        for i in request.data[' assing_info']:
            i1 = student_model.objects.get(stu_name=i['stu_name'])
            assing.objects.assing_info.add(i1)
        response = {
            'message': 'created'
        }
        return Response(response)


def latest_trend(created_date):
    print("creates dataa")
    trend_date = datetime.datetime.fromtimestamp(int(created_date / 1000))
    current_datetime = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=20)
    print(trend_date, "trend date", current_datetime)
    if current_datetime > trend_date:
        print(" old trend  ")
        return False
    else:
        print("latest ")
        return True


class twitter(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def twitter_trend(self, request, index, country):
        user = request.user
        print('user request', user)
        if 'country' in request.data:
            country = request.data['country']
        else:
            country = 'argentina'

        try:
            res = ess_object.twitter_trend(
                index='twitter_trends',
                country=country
            )
            latest = latest_trend(res[0]['created_on'])
            if latest:
                response = {
                    'message': 'latest',
                    'status': True,
                    'result': res

                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {'message': 'google trends',
                            "Alert": " trends are not latest",
                            'status': True,
                            'result': res
                            }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as E:
            print(E)
            response = {'message': 'Error',
                        'status': True,
                        'result': str(E)
                        }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


# class func6_veiw(ModelViewSet):
#     def create(self):
