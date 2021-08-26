from resume_creator.models import Education, Information, Work
from django.shortcuts import render

from .forms import RegistrationForm
from .forms import EducationForm
from .forms import WorkForm

# Create your views here.
def index(request):
    return render(request, 'resume_creator/index.html')

def personal_info(request):
    try:
        print('entered try')
        if request.method == 'GET':
            print('if')
            registration_form = RegistrationForm()
            education_form = EducationForm()
            work_form = WorkForm()
        else:
            registration_form = RegistrationForm(request.POST)
            education_form = EducationForm(request.POST)
            work_form = WorkForm(request.POST)
            print('entered else')
            if registration_form.is_valid() and education_form.is_valid() and work_form.is_valid():
                registerer = registration_form.save()

                degree = education_form.cleaned_data['degree']
                stream = education_form.cleaned_data['stream']
                passing_year = education_form.cleaned_data['passing_year']
                edu = Education(person=registerer, degree=degree, stream=stream, passing_year=passing_year)
                edu.save()

                title = work_form.cleaned_data['title']
                company = work_form.cleaned_data['company']
                description = work_form.cleaned_data['description']
                work = Work(person=registerer, title=title, company=company, description=description)
                work.save()

                return render(request, 'resume_creator/output.html', {
                    'info' : registerer,
                    'edu' : edu,
                    'work' : work
                })

        return render(request, 'resume_creator/personal_info.html', {
            'form': registration_form,
            'edu_form': education_form,
            'work_form': work_form
        })
    
    except Exception as e:
        print(e)
        return render(request,'resume_creator/error.html' )

#def resume(request):
#    return render(request, 'resume_creator/output.html')

def home(request):
    return render(request, 'resume_creator/home.html')