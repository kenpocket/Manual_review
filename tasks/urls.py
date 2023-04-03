from django.urls import path
from . import views
urlpatterns = {
    path('_01', views.task_1),
    path('_01', views.task_1),
    path('_01/next', views.next_page),
    path('_02', views.task_2),
    path('process_true', views.process_true),
    path('process_false', views.process_false),
}