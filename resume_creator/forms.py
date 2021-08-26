from django import forms

from .models import Education, Information, Work

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['f_name', 'l_name', 'address', 'city', 'state', 'zip', 'email']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'stream', 'passing_year']

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'company', 'description']
