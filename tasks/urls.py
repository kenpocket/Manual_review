from django.urls import path
from . import views
urlpatterns = {
    path('_01', views.task_1),
    path('_02', views.task_2),
}