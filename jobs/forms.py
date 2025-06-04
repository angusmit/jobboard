from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location', 'email']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class JobSeekerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'jobseeker'
        if commit:
            user.save()
        return user

class EmployerSignUpForm(UserCreationForm):
    company = forms.CharField(max_length=100)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'company')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'employer'
        user.company = self.cleaned_data['company']
        if commit:
            user.save()
        return user