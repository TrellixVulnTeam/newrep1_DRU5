from rest_framework.routers import SimpleRouter
from .models import student_model, projects
from .views import func_viewset, func2_view, func3_veiw,func4_veiw,func5_veiw
from django.urls import path, include

router = SimpleRouter()
router.register('viewset', func_viewset)
router.register('viewset2', func2_view)
router.register('viewset3', func3_veiw)
router.register('viewset4', func4_veiw)
router.register('viewset5', func5_veiw)

urlpatterns = [
    path('func/', include(router.urls)),

]
