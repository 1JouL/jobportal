from django.db import models
from django.conf import settings
# from .models import Job

# Create your models here.
JOB_TYPE_CHOICES = [
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Internship','Internship'),
    ('Contract','Contract')
]

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50,choices=JOB_TYPE_CHOICES)
    salary = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    deadline =models.DateField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"


APPLICATION_STATUS_CHOICES = [
    ('applied','Applied'),
    ('shortlisted','Shortlisted'),
    ('interview','L1 Cleared'),
    ('interview_technical','Interview technical'),
    ('hr_cleared','HR Cleared'),
    ('rejected','Rejected'),
    ('offered','Offered'),
    ('on_hold','On Hold')
]

class JobApplication(models.Model):
    jobs = models.ForeignKey('Job',on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=APPLICATION_STATUS_CHOICES,default='applied')
    status_notified = models.BooleanField(default=True)

    class Meta:
        unique_together = ('jobs','student')

    def __str__(self):
        return f"{self.student.email}+{self.jobs.title}"