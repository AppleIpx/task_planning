from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserView, basename="users")
router.register(r'task_plan', views.TasksPlanView, basename="task_plan")

urlpatterns = [
    path(r'auth/', include('djoser.urls.authtoken')),
    path("", include(router.urls)),
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
