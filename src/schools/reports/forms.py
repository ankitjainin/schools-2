# -*- coding: utf-8 -*-
from django import forms
from django.forms.util import ValidationError
from django.utils.translation import ugettext as _
from schools.companies.models import Company


class InvoiceForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()
    companies = forms.ModelMultipleChoiceField(queryset=Company.objects.all(), required=False)
    show_students = forms.BooleanField(required=False)
    
    def __init__(self, companies, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['companies'].queryset = companies
    
    def clean(self):
        if 'start' in self.cleaned_data and 'end' in self.cleaned_data:
            if not self.cleaned_data['start'] <= self.cleaned_data['end']:
                raise ValidationError(_(u'Začiatok musí byť menší ako koniec'))
        return self.cleaned_data
    
class LessonAnalysisForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()
    show_courses = forms.BooleanField(required=False)
    
    def clean(self):
        if 'start' in self.cleaned_data and 'end' in self.cleaned_data:
            if not self.cleaned_data['start'] <= self.cleaned_data['end']:
                raise ValidationError(_(u'Začiatok musí byť menší ako koniec'))
        return self.cleaned_data
    
class RangeForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()
    
    def clean(self):
        if 'start' in self.cleaned_data and 'end' in self.cleaned_data:
            if not self.cleaned_data['start'] <= self.cleaned_data['end']:
                raise ValidationError(_(u'Začiatok musí byť menší ako koniec'))
        return self.cleaned_data
LessonPlanForm = RangeForm

class CompanyAddedValueForm(forms.Form):
    start = forms.DateField()
    end = forms.DateField()
    companies = forms.ModelMultipleChoiceField(queryset=Company.objects.all(), required=False)
    
    def clean(self):
        if 'start' in self.cleaned_data and 'end' in self.cleaned_data:
            if not self.cleaned_data['start'] <= self.cleaned_data['end']:
                raise ValidationError(_(u'Začiatok musí byť menší ako koniec'))
        return self.cleaned_data