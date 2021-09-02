from django.urls import path
from rest_framework import viewsets
from rest_framework import routers
from . import views
from django.urls import include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,basename='login')
router.register('task',views.TaskViewset)
urlpatterns = [
    path('helloview/',views.HelloAPIView.as_view()),
    path('',include(router.urls)),
]
