from datetime import datetime

from django.shortcuts import render
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from . import elastic
from serializer import NewsCrawelerSerializer
from rest_framework.response import Response
from django.http import HttpResponse

from .elastic import search

# Create your views here.
obj_es = elastic.search()


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


class func(ModelViewSet):

    def func(self, request, channel, size, ):
        # post function
        user = request.user
        print('user print', user)
        seri = NewsCrawelerSerializer(data=request.data)
        data_t = seri.data.copy()
        result = [*data_t]
        if set(result) == {'channel', 'size'}:
            channel, size = data_t['channel'], data_t['size']
            res = obj_es.search(index='twitter_trends', channel=channel, size=size)
            response = {
                'message': 'yes',
                'status': True,
                'result': res
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'message': 'yes',
                'status': True,
                'result': None
            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)

    def func2(self, request, index, country, size):
        user = request.user
        print('user request', user)
        seri = NewsCrawelerSerializer(data=request.data)
        data_dic = seri.data.copy()
        key = [*data_dic]
        if set(key) == {'country', 'size'}:
            country, size = data_dic['country'], data_dic['size']
            obj = obj_es.youtube_trends(index='youtube_index', country=country, size=size)
            if obj:
                response = {
                    'message': 'done',
                    'status': True,
                    'result': obj

                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'message': 'error',
                    'status': True,
                    'result': obj

                }

                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {
                'message': 'nothing',
                'status': True,
                'result': None

            }
            return Response(response, status=status.HTTP_204_NO_CONTENT)

    def disp_twitter_latest(self, request):
        user = request.user
        print('user content', user)
        try:
            result = obj_es.disp_twitter_trends(index='tweitter_trend', gte=1000, lte=100000)
            if result:
                response = {
                    'message': 'done',
                    'status': True,
                    'result': result

                }
                return Response(response, status.HTTP_200_OK)
            else:

                response = {
                    'message': 'nothing',
                    'status': True,
                    'result': result

                }
                return Response(response, status.HTTP_200_OK)



        except Exception as error:
            print(error)

    def google_trends(self, request):
        user = request.user
        print('user request', user)
        try:

            result = obj_es.google_trends_elasticsearch(index='google-trends')
            res = latest_trend(result[0]['created_on'])
            if res:
                response = {
                    'message': 'latest',
                    'status': True,
                    'result': result

                }
                return Response(response, status.HTTP_200_OK)
            else:
                send_event('notification', 'message', {"Notification_message": "Twitter trends are not latest"})
                response = {
                    'message': 'no latest',
                    'status': True,
                    'result': result

                }
                return Response(response, status.HTTP_200_OK)
        except Exception as E:
            print(E)
            response = {
                'message': 'no latest',
                'status': True,
                'result': str(E)

            }
            return Response(response, status.HTTP_200_OK)



            # def twitter(self, request, channel, size):
            #     user = request.user
            #     print('user request', user)
            #     seri = NewsCrawelerSerializer(data=request.data)
            #     data_dic = seri.data.copy()
            #     result = [*data_dic]
            #
            #     try:
            #         if set(result) == {'channel', 'size'}:
            #             channel, limit = data_dic['channel'], data_dic['limit']
            #             obj = obj_es.search(index='twitter', channel=channel, size=size)
            #             response={
            #
            #                 'message':'content',
            #                 'status':True,
            #                 'result':obj
            #             }
            #             return Response(response,status=status.HTTP_200_OK)
            #
            #
            #     except Exception as E:
            #         response = {'message': 'Error while Getting Response',
            #                     'status': True,
            #                     'result': str(E)}
            #         return Response(response,status=status.HTTP_200_OK)
            #
            #
            #
