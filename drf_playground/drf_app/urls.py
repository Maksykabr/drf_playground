from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import rest_framework



router = routers.SimpleRouter()
router.register(r'universities', views.UniversityViewsSet)
router.register(r'profiles', views.ProfilesViewsSet)
router.register(r'userCreate', views.UserCreateView)
router.register(r'usersList', views.UsersViewsSet)





urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]