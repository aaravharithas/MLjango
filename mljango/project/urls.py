from django.urls import path
from . import views

urlpatterns = [
    path('ML001',views.iris_ML001,name='project-ML001'),
    path('ML002',views.emotion_ML002,name='project-ML002'),
    path('ML003',views.cardio_ML003,name='project-ML003'),
]