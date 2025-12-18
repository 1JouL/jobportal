from django import forms
from .models import Job
import datetime
class JobPostForm(forms.ModelForm):
    class Meta:
        model =Job
        fields = ['title','description','company','location','job_type','deadline','salary']
        widgets ={
            'description':forms.Textarea(attrs={'rows':4}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type':'date', 'min': datetime.date.today().strftime('%Y-%m-%d')}),
        }

        def __init__(self,*args,**kwargs):
            super(JobPostForm,self).__init__(*args,**kwargs)
            for field in self.fields.values():
                field.wedget.attrs.update({'class':'form-control'})
            