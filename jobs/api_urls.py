from  django.urls import path
from .import api_views


urlpatterns =[
    path('jobs/',api_views.job_list_view,name='job_list_view'),
    path('jobs/<int:id>/',api_views.job_detial,name='job_detial'),
    path('job_create/',api_views.job_create1,name='job_create1'),
    path('jobs_edit/<int:id>/',api_views.job_update,name='jobs_edit'),
    path('jobs_delete/<int:id>/',api_views.job_delete,name='jobs_delete')
]