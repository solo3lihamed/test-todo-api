from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('', include(router.urls)),
]
