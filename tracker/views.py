from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Issue
from .forms import ProjectForm, IssueForm
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import login


def home(request):
    return render(request, 'tracker/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'tracker/logout.html')

def login_view(request):
    login(request)
    return render(request, 'tracker/login.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tracker/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'tracker/project_detail.html', {'project': project})

def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'tracker/issue_detail.html', {'issue': issue})

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'tracker/project_form.html', {'form': form})

def create_issue(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.project = project
            issue.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = IssueForm()
    return render(request, 'tracker/issue_form.html', {'form': form, 'project': project})
