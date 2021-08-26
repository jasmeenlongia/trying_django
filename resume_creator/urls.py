from django.urls import path

from . import views

urlpatterns = [
    path('resume_creator/', views.index, name = "start"),
    path('resume_creator/home', views.home, name = "start1"),
    path('resume_creator/personal_info', views.personal_info, name = "personal"),
    #path('resume_creator/final_resume', views.resume, name = "final_resume"),
]