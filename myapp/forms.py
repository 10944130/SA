from django import forms
from .models import Issue, Report
from .models import qa

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description']

class qaForm(forms.ModelForm):
    class Meta:
        model = qa
        fields = ['DISC', 'IMAGE']

class ReportForm(forms.ModelForm):
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 0:
            raise forms.ValidationError('請輸入問題')
        return description

    class Meta:
        model = Report
        fields = [ 'description', 'image']



