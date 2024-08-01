from django import forms
from .models import Project, Issue

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'image']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'status', 'assigned_to']

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'image']

class IssueEditForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'status', 'assigned_to']
