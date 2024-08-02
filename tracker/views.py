from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Project, Issue
from .forms import ProjectForm, IssueForm, ProjectEditForm, IssueEditForm

def home(request):
    return render(request, 'tracker/home.html')

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tracker/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'tracker/project_detail.html', {'project': project})

@login_required
def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'tracker/issue_detail.html', {'issue': issue})

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'tracker/project_form.html', {'form': form})

@login_required
def create_issue(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.project = project
            issue.save()
            return redirect('project_detail', pk=project.pk)
        else:
            print(f"Form errors: {form.errors}")  # Debugging line
    else:
        form = IssueForm()
    return render(request, 'tracker/issue_form.html', {'form': form, 'project': project, 'is_edit': False})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectEditForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectEditForm(instance=project)
    return render(request, 'tracker/project_form.html', {'form': form})

@login_required
def edit_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        form = IssueEditForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=issue.pk)
        else:
            print(f"Form errors: {form.errors}")  # Debugging line
    else:
        form = IssueEditForm(instance=issue)
    return render(request, 'tracker/edit_issue_form.html', {'form': form, 'issue': issue, 'project': issue.project, 'is_edit': True})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
