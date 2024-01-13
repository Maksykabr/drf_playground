from django.urls import path, include
from . import views
from rest_framework import routers
import rest_framework


router = routers.SimpleRouter()
router.register(r'universities', views.UniversityViewsSet)
router.register(r'profiles', views.ProfilesViewsSet)
router.register(r'userCreate', views.UserCreateView)
router.register(r'usersList', views.UsersViewsSet)
# router.register(r'login', include("rest_framework.urls"))
# router.register(r'user_create', views.UserCreateView, basename=register)




urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
    
    # path('login/', views.LoginView.as_view(), name='login')
    #  path('register/', views.UserCreateView.as_view(), name='register'),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
]