from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import mixins, generics
from .models import aeroplane
from .serialize import aeroplane_serializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import permission_required
from rest_framework.response import Response


class ListProductMixins(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                        mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    queryset = aeroplane.objects.all()
    serializer_class = aeroplane_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EditBlogView(PermissionRequiredMixin, View):
    permission_required = 'aeroplane.view_aeroplane'
    def get_permission_required(self):
        perms = super(EditBlogView, self).get_permission_required()
        return perms

    def has_permission(self):
        perms = super(EditBlogView, self).has_permission()
        return perms

    def get(self, request, *args, **kwargs):

        return HttpResponse('heloooo')
