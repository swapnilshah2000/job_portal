from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from job.filter import JobFilter
from job.models import Job, JobApplicants
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def job_list(request):
    job_type_dict = {}
    job_type_list = ['full-time',
                    'part-time',
                    'self-employed',
                    'frelance',
                    'contract',
                    'internship']
    for i in job_type_list:
        job_type_count = Job.objects.filter(job_type=i).count()
        job_type_dict[i] = job_type_count

    #Filter 
    filter_job = JobFilter(request.GET, queryset=Job.objects.all())
    paginator = Paginator(filter_job.qs,2)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)

    context = {
        'filter' : filter_job,
        'job_type_dict' : job_type_dict,
        'paged_list' : paged_list
    }
    return render(request,'job/job_list.html',context)


def job_detail(request,id): 
    job_detail = Job.objects.get(id=id)
    context = {
        'job_detail' : job_detail,
    }
    return render(request,'job/job_detail.html',context)

@login_required
def job_apply(request):
    if request.method == 'POST':
        job_id = request.POST.get('id')
        job_instance_id = Job.objects.get(id=job_id)
        if job_instance_id.applicants_collection_mode == 'email':    
            JobApplicants.objects.create(candidate_id=request.user,job_id=job_instance_id)
            # send_mail(
            #     'Inquiry for Job',
            #     f"There has been an inquiry for job aaplication. Name: {request.user}",
            #     'joshijaya.shivinfotech@gmail.com',
            #     ('joshijaya29@gmail.com',job_instance_id.applicants_collection_link_email,),
            #     fail_silently=False
            #     ) 
            messages.success(request, f'Successfully apply for {job_instance_id} job at {job_instance_id.company_id.name}')
            return redirect('job_list')
        else: 
            JobApplicants.objects.create(candidate_id=request.user,job_id=job_instance_id)

            return redirect(job_instance_id.applicants_collection_link_email)
    else: 
        return HttpResponseRedirect('signup',request.META.get('HTTP_REFERER'))  
        
  