import django_filters
from django import forms
from job.models import Job
from master_table.models import Location
from options import Experience_job_type

class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={'name':"search", 'id':"searchname", 'type':"text", 'class':"form-input border border-slate-100 dark:border-slate-800 ltr:pl-10 rtl:pr-10", 'placeholde':"Search"}))
    location_id = django_filters.ModelChoiceFilter(queryset=Location.objects.all(),widget=forms.Select(attrs={'class':"form-select form-input border border-slate-100 dark:border-slate-800 block w-full mt-1"}))
    job_type = django_filters.MultipleChoiceFilter(choices=Experience_job_type,lookup_expr='icontains',widget=forms.CheckboxSelectMultiple(attrs={'name':"search", 'id':"searchname", 'type':"checkbox", 'class':"form-checkbox border border-slate-100 dark:border-slate-800 text-emerald-600 rounded w-4 h-4", 'placeholde':"Search"}))
    salary = django_filters.NumberFilter()
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt',widget=forms.TextInput(attrs={'name':"search", 'id':"searchname", 'type':"text", 'class':"form-input border border-slate-100 dark:border-slate-800 ltr:pl-10 rtl:pr-10", 'placeholde':"Search"}))
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt',widget=forms.TextInput(attrs={'name':"search", 'id':"searchname", 'type':"text", 'class':"form-input border border-slate-100 dark:border-slate-800 ltr:pl-10 rtl:pr-10", 'placeholde':"Search"}))

    class Meta:
        model = Job
        fields = ['job_title','location_id','job_type','salary','salary__lt','salary__gt']



