from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm

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