from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('enviar/', views.feedback_create, name='feedback_create'),
]
