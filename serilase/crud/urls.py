from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views
from .views import student_view

routers = DefaultRouter()
routers.register('crud', student_view)
# routers.register('crud2', viewstudent)
urlpatterns = [
    path('api/', include(routers.urls))

]

router_ = SimpleRouter()
router_.register('delete', student_view)
urlpatterns += [
    path('api/delete_/<int:id>', views.student_view.as_view({'delete': 'delete_'}), name='delete_'),
    path('api/create_/', views.student_view.as_view({'post': 'create_'}), name='create')

]
