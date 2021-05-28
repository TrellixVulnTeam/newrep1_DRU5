from rest_framework.routers import SimpleRouter
from django.urls import include, path
from . import views
from .views import four

router = SimpleRouter()
# router.register('third', four)


urlpatterns = [
    path("test/", views.four.as_view())

    # path('se/', include(router.urls))
]
