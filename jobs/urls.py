from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.job_create,name='job_create'),
    path('view_all_job/',views.view_All_Job,name='view_all_Job'),
    path('job/<int:id>/',views.job_detail,name='job_detail'),
    path('job_apply/<int:id>/',views.apply_job,name='apply_job'),
    path('recruiter/jobs',views.recruiter_job,name='recruiter_job'),
    path('edit/<int:job_id>/',views.edit_job,name='edit_job'),
    path('delete/<int:job_id>/',views.delete_job,name='delete_job'),
    path('applicats/<int:job_id>',views.view_applicants,name='view_applicants'),
    path('application/update/<int:application_id>/',views.update_application_status,name='update_application_status'),
]