from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'users', views.UserViewSet,basename='user')
router.register(r'groups', views.GroupsViewSet,basename='groups')
router.register(r'notes', views.NotesViewSet,basename='notes')
router.register(r'appointments', views.AppointmentViewSet,basename='appointments')

urlpatterns = [
    path('', include(router.urls))
]
