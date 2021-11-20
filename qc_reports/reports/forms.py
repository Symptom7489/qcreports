from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Project, QCReport, JMF, CoreReadings, NRSetup
from django.db import models
from datetime import datetime

class DateSelectDefaultNow(forms.DateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        # Ensure attrs kwargs exists
        kwargs['attrs'] = kwargs.get('attrs', {})
        # Set our defaults
        kwargs['attrs'].update({
            'value': datetime.now().strftime("%Y-%m-%d"),
        })
        super().__init__(*args, **kwargs)

        
class DateInput(forms.DateInput):
    input_type = 'date'

class CheckBoxInput(forms.CheckboxSelectMultiple):
    input_type = 'check_box'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'barber_number', 'state_number', 'project_name',
            'jmfs'
        ]

        widgets = {
            'jmfs': CheckBoxInput(),
        }

class JmfForm(ModelForm):
    class Meta:
        model = JMF
        fields = ('__all__')

        widgets = {
            'project_name': CheckBoxInput(),
        }


class DateInput(forms.DateInput):
    input_type = 'date'

class CoreReadingsForm(ModelForm):
    class Meta:
        model = CoreReadings
        fields = ['project', 'jmf', 'job_type', 'core_type', 'core_lot', 'core_id', 'core_location',
                      'lane_direction', 'gauge_reading_1','gauge_reading_average', 'date_time',
                      ]
        labels = {
            'gauge_reading_1': 'One Shot Reading',
        }

        widgets = {
            'date_time' : DateInput()
        }


class QCReportForm(ModelForm):
    class Meta:
        model = QCReport
        fields = ('project', 'jmf', 'readings', 'notes', 'report_date')
        widgets = {
            'report_date': DateInput(),
            'project': CheckBoxInput(),
            'jmf': CheckBoxInput(),
            'readings': CheckBoxInput(),
        }


# NightlyReadingsFormset = modelformset_factory(NightlyReadings ,fields=('nightly_readings',), extra=numberOfEntities)
# jmf_list = JMF.objects.jmf_number
# project_list =

class Setup(forms.Form):
    jmf = forms.ModelChoiceField(
        queryset=JMF.objects.all()
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all()
    )
    number_of_entries = forms.IntegerField()
    date = forms.DateField(
        widget=DateSelectDefaultNow()
    )



# class NRSetup(ModelForm):
#     class Meta:
#         model = NRSetup
#         fields = ('project','jmf','numberOfEntries','date')
#
#         labels = { 'numberOfEntries': 'Number of Readings'}
#
#         widgets = { 'date': DateInput(),
#                     'jmf': CheckBoxInput,
#                     'project': CheckBoxInput
#                     }





