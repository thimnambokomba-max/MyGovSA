from django.urls import path
from . import views
 
urlpatterns = [
    path('report/', views.report_step1, name='report_step1'),
    path('report/step2/', views.report_step2, name='report_step2'),
    path('report/step3/', views.report_step3, name='report_step3'),
    path('track/', views.track_issue, name='track_issue'),
]