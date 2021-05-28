"""serilase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from signals import views
from newnew import views

# from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('app1/func', views.carview.as_view({'get': 'func'}), name='app1'),
    # path('app1/func2', views.carview.as_view({'get': 'func2'}), name='app1'),
    # path('app1/func3', views.carview.as_view({'post': 'func3'}), name='app1'),
    # path('app1/delete_details/<int:pk>', views.carview.as_view({'delete': 'delete_details'}), name='app1'),
    # path('app1/overwrite_details/<int:num>', views.carview.as_view({'put': 'overwrite_details'}), name='app1'),
    # path('app1/partial_update/<int:num>', views.carview.as_view({'patch': 'partial_update'}), name='app1'),
    path('', include('crud.urls')),
    # path('', include('custom.urls')),
    # path('', include('test_1.urls')),
    # path('custom/sec', views.four.as_view({'get': 'store_manager'}), name='store'),
    # path('signals/', views.home),
    # path('prin/', views.prin),
    path('mixin/<int:pk>', views.ListProductMixins.as_view(), name='mp'),
    path('edit-blog/', views.EditBlogView.as_view(), name='edit-blog'),
]
