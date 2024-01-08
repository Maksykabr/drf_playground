from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'universities', views.UniversityViewsSet)
router.register(r'teachers', views.TeachersViewsSet)
router.register(r'students', views.StudentsViewsSet)
router.register(r'profiles', views.ProfileViewsSet)
router.register(r'createUser', views.ProfileCreateUserView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
]