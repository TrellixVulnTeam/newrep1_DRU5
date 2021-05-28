from rest_framework.routers import SimpleRouter
from django.urls import include, path
from . import views
from .views import func, project_class, student_class

router = SimpleRouter()
router.register('func', func)
router.register('proj', project_class)
router.register('stu', student_class)

urlpatterns = [
    path('c/', include(router.urls)),
    path('cc/<int:id>', views.func.as_view({'put': 'up'}), name="up"),
    path('new/', include(router.urls))

]
