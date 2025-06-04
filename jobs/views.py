from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import JobSeekerSignUpForm, EmployerSignUpForm
from django.contrib.auth.decorators import login_required

def job_list(request):
    jobs = Job.objects.filter(is_approved=True)
    
    # Basic search
    query = request.GET.get('q')
    location = request.GET.get('location')
    
    if query:
        jobs = jobs.filter(title__icontains=query) | jobs.filter(description__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

def job_post(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.is_approved = False  # Needs admin approval
            job.save()
            return render(request, 'jobs/job_post_success.html')
    else:
        form = JobForm()
    return render(request, 'jobs/job_post.html', {'form': form})



def signup(request):
    return render(request, 'jobs/signup.html')

def jobseeker_signup(request):
    if request.method == 'POST':
        form = JobSeekerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = JobSeekerSignUpForm()
    return render(request, 'jobs/jobseeker_signup.html', {'form': form})

def employer_signup(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = EmployerSignUpForm()
    return render(request, 'jobs/employer_signup.html', {'form': form})



@login_required
def job_post(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user  # Set current user as employer
            job.is_approved = False
            job.save()
            return render(request, 'jobs/job_post_success.html')
    else:
        form = JobForm()
    return render(request, 'jobs/job_post.html', {'form': form})