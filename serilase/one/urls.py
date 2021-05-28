from rest_framework.routers import SimpleRouter
from django.urls import include, path
from . import views
from .views import func1, third_view

router = SimpleRouter()
router.register('newfunc', func1)
# router.register('fun', second_view)
router.register('newfunc', third_view)

urlpatterns = [

    path('car/create', views.func1.as_view({'post': 'create'}), name='car'),
    path('c/', include(router.urls)),

]
