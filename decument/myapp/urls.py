from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    path('user/',views.UserView.as_view()),
    path('plan/',views.Previous_planView.as_view()),
    path('plan/<int:pk>/',views.PlanDetail.as_view()),
    # path('download/',views.PlanDetail.as_view()),
    path('download/<int:pk>/',views.DownloadView.as_view()),
    path('allplan/',views.AllPlanView.as_view()),
    path('allplan/<int:pk>/',views.PlanDelete.as_view()),
    path('document/',views.DocView.as_view()),
    path('test/',views.TestView.as_view()),
]