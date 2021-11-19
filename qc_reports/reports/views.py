import datetime
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from .forms import ProjectForm, JmfForm, CoreReadingsForm
from .forms import QCReportForm, Setup
from django.http import HttpResponseRedirect
from .models import Project, JMF, NightlyReadings
from django.forms import modelformset_factory

# Create your views here.

#Chart.js page
def test_data(request):
    project_list = list(Project.objects.values())
    return JsonResponse(project_list, safe=False)


def show_jmfs(request, jmf_id):
    jmfs = JMF.objects.get(pk=jmf_id)
    projects = Project.objects.filter(jmfs__exact=jmfs)
    return render(request, 'reports/show_jmfs.html', {'jmfs': jmfs,'projects':projects, })


def show_projects(request, project_id):
    all_jmfs = JMF.objects.all
    project = Project.objects.get(pk=project_id)
    jmf_list = project.jmfs.all
    return render(request, 'reports/show_projects.html', {'project': project, 'jmf_list':jmf_list, 'all_jmfs': all_jmfs})

def home(request):
    jmf_list = JMF.objects.all()
    project_list = Project.objects.all()
    return render(request, 'reports/index.html', {'project_list':project_list, 'jmf_list':jmf_list})

def add_project(request):
    submitted = False
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_project?submitted=True')
    else:
        form = ProjectForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'reports/add_project.html', {'form': form, 'submitted': submitted})

def add_jmf(request):
    submitted = False
    if request.method == 'POST':
        form = JmfForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_jmf?submitted=True')
    else:
        form = JmfForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'reports/add_jmf.html', {'form': form, 'submitted': submitted})

def add_readings(request):
    submitted = False
    if request.method == 'POST':
        form = CoreReadingsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_readings?submitted=True')
    else:
        form = CoreReadingsForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'reports/add_readings.html', {'form': form, 'submitted': submitted})

def add_qcreport(request):
    submitted = False
    if request.method == 'POST':
        form = QCReportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/qc_report?submitted=True')
    else:
        form = QCReportForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'reports/qc_report.html', {'form': form, 'submitted': submitted})

def update_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    submitted = False
    setup = False
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_jmf?submitted=True')
    else:
        form = ProjectForm(instance=project)
        if 'submitted' in request.GET:
            submitted = True
            update= True
    return render(request, 'reports/add_jmf.html', {'form': form, 'submitted': submitted,})


def nightly_form(request):
    numberOfEntries = 5
    submitted = False
    setup = False
    if request.method == 'POST':
        NightlyReadingsFormset = modelformset_factory(NightlyReadings, fields=('nightly_readings',),
                                                      extra=numberOfEntries)

        # if request.method == 'POST' and setup == False:
        setup = True
        form = Setup(request.POST)
        ryan = 'Ryan'
        if form.is_valid():
            jmf = form.cleaned_data['jmf']
            project = form.cleaned_data['project']
            numberOfEntries = form.cleaned_data['numberOfEntries']
            date = form.cleaned_data['date']

        formset = NightlyReadingsFormset
        return render(request, 'reports/nightly_form.html', {'formset':formset, 'setup':setup, 'jmf':jmf,'project':project,'numberOfEntries':numberOfEntries, 'ryan':ryan })

    # elif request.method == 'POST' and submitted == True:
    #     formset = NightlyReadingsFormset(request.POST)
    #     if formset.is_valid():
    #         instance = formset.save()
    #
    #     return render(request, 'reports/nightly_form.html')



    else:
        jmfs = JMF.objects.all
        projects = Project.objects.all
        form = Setup
        return render(request, 'reports/nightly_form.html', {'form':form, 'jmfs':jmfs,'projects':projects})
