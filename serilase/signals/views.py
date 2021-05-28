from django.shortcuts import render, HttpResponse
from signals.signalsfile import notification


# Create your views here.


def home(request):
    notification.send(sender=None, request=request, user=['geeks', 'shows'])
    return HttpResponse('this is homepage')
