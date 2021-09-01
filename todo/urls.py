from django.urls import path
from . import views

urlpatterns = [
    path('helloview/',views.HelloAPIView.as_view()),
]
