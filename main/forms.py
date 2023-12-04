from django import forms
from main.models import *

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ("imprint","main_publisher",)

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ("name","pissn","eissn","publisher","remark",)