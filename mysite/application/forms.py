from django import forms
from django.forms import ModelForm
#from .models import Post
from .models import Testbed
from .models import Script
from .models import ScriptsTestbedSupport
from django.contrib.admin import widgets                                       
#from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import HiddenInput, IntegerField, CharField
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from variables import *

class ScriptForm(forms.ModelForm):
    #tb_reserved_till_datetime = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'],widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    testbeds_slug = CharField(widget=HiddenInput()) # Pointer Back to Family
    order = IntegerField(required=False, widget=HiddenInput(), initial=0)
    class Meta:
        model = Script
        fields = ('script_id', 'script_name','status_id' ,'script_status_comments', 'testbeds')

    '''def __init__(self, *args, **kwargs):
        super(ScriptForm, self).__init__(*args, **kwargs)
        self.fields['script_id'].error_messages = {'required': 'custom required message'}
        #self.fields['tb_reserved_till_datetime'].widget = widgets.AdminSplitDateTime()
        #self.fields['tb_status_reservation_time'].widget = widgets.AdminSplitDateTime()
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}'''
    
    def save(self, commit=True):
        
        scripts = super(ScriptForm, self).save #save the child so we have an id for m2m
        
        testbeds_slug = self.cleaned_data.get('script_slug')
        testbeds = Testbed.objects.get(slug=testbeds_slug)
        ScriptsTestbedSupport.objects.create(testbeds=testbeds, scripts=scripts)

        return scripts
        #ModelForm
class ScriptForm1(ModelForm):
    #testbeds = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Script
        fields = ['script_id', 'script_name','status_id', 'script_status_comments', 'request', 'script_version', 'script_repo','script_branch','testbeds']
        widgets = {
           'script_name': forms.TextInput(attrs={'size':'60'}),
           'script_status_comments': forms.TextInput(attrs={'size':'60'}),
           'request': forms.TextInput(attrs={'size':'60'}),
           'script_version':forms.TextInput(attrs={'size':'60'}),
           'script_repo':forms.TextInput(attrs={'size':'60'}),
           'script_branch':forms.TextInput(attrs={'size':'60'}),
         }
    def __init__(self, *args, **kwargs):

        super(ScriptForm1, self).__init__(*args, **kwargs)

        self.fields["testbeds"].widget = CheckboxSelectMultiple()
        self.fields["testbeds"].queryset = Testbed.objects.filter(~Q(tb_id__in=hidden_script_ids))
        self.fields["testbeds"].required = False


class RegistrationForm(ModelForm):
    script_name = forms.CharField(help_text ='Provide unique script name * Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    script_status_comments =forms.CharField(help_text ='Provide comment for script, eg: - Added Script. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    request = forms.CharField(help_text ='Provide request for script, eg: - REG-1234. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    script_version = forms.CharField(initial='1', help_text ='Provide version for script, eg: - 1, 2. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    script_repo  = forms.CharField(initial='regscript', help_text ='provide repo for script, eg: - regscript. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))   
    script_branch  = forms.CharField(initial='master', help_text ='Provide branch for script, eg: - master. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    testbeds = forms.ModelMultipleChoiceField(queryset=Testbed.objects.filter(~Q(tb_id__in=hidden_script_ids)).order_by('tb_name'),widget=forms.CheckboxSelectMultiple,required=False,help_text= 'Check testbed(s) to map with script, *Optional')
    class Meta:
        model = Script
        fields = ['script_id', 'script_name','status_id', 'script_status_comments', 'request','script_version', 'script_repo','script_branch','testbeds',]
        widgets = {
           'status_id': forms.HiddenInput(),
           }
        help_texts = {
           'script_id': 'Provide unique script id, only digits are allowed. * Mandatory',
           'status_id': 'Select one option out of following - Submitted, New, Production, Decommissioned. * Mandatory',
           }
        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
from django import forms
from django.forms import ModelForm
#from .models import Post
from .models import Testbed
from .models import Script
from .models import ScriptsTestbedSupport
from django.contrib.admin import widgets                                       
#from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import HiddenInput, IntegerField, CharField
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from variables import *

class ScriptForm(forms.ModelForm):
    #tb_reserved_till_datetime = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'],widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","pickSeconds": False}))
    testbeds_slug = CharField(widget=HiddenInput()) # Pointer Back to Family
    order = IntegerField(required=False, widget=HiddenInput(), initial=0)
    class Meta:
        model = Script
        fields = ('script_id', 'script_name','status_id' ,'script_status_comments', 'testbeds')

    '''def __init__(self, *args, **kwargs):
        super(ScriptForm, self).__init__(*args, **kwargs)
        self.fields['script_id'].error_messages = {'required': 'custom required message'}
        #self.fields['tb_reserved_till_datetime'].widget = widgets.AdminSplitDateTime()
        #self.fields['tb_status_reservation_time'].widget = widgets.AdminSplitDateTime()
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}'''
    
    def save(self, commit=True):
        
        scripts = super(ScriptForm, self).save #save the child so we have an id for m2m
        
        testbeds_slug = self.cleaned_data.get('script_slug')
        testbeds = Testbed.objects.get(slug=testbeds_slug)
        ScriptsTestbedSupport.objects.create(testbeds=testbeds, scripts=scripts)

        return scripts
        #ModelForm
class ScriptForm1(ModelForm):
    #testbeds = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Script
        fields = ['script_id', 'script_name','status_id', 'script_status_comments', 'request', 'script_version', 'script_repo','script_branch','testbeds']
        widgets = {
           'script_name': forms.TextInput(attrs={'size':'60'}),
           'script_status_comments': forms.TextInput(attrs={'size':'60'}),
           'request': forms.TextInput(attrs={'size':'60'}),
           'script_version':forms.TextInput(attrs={'size':'60'}),
           'script_repo':forms.TextInput(attrs={'size':'60'}),
           'script_branch':forms.TextInput(attrs={'size':'60'}),
         }
    def __init__(self, *args, **kwargs):

        super(ScriptForm1, self).__init__(*args, **kwargs)

        self.fields["testbeds"].widget = CheckboxSelectMultiple()
        self.fields["testbeds"].queryset = Testbed.objects.filter(~Q(tb_id__in=hidden_script_ids))
        self.fields["testbeds"].required = False


class RegistrationForm(ModelForm):
    script_name = forms.CharField(help_text ='Provide unique script name * Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    script_status_comments =forms.CharField(help_text ='Provide comment for script, eg: - Added Script. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    request = forms.CharField(help_text ='Provide request for script, eg: - REG-1234. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    script_version = forms.CharField(initial='1', help_text ='Provide version for script, eg: - 1, 2. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    script_repo  = forms.CharField(initial='regscript', help_text ='provide repo for script, eg: - regscript. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))   
    script_branch  = forms.CharField(initial='master', help_text ='Provide branch for script, eg: - master. *Mandatory', widget=forms.TextInput(attrs={'size':'60'}))
    testbeds = forms.ModelMultipleChoiceField(queryset=Testbed.objects.filter(~Q(tb_id__in=hidden_script_ids)).order_by('tb_name'),widget=forms.CheckboxSelectMultiple,required=False,help_text= 'Check testbed(s) to map with script, *Optional')
    class Meta:
        model = Script
        fields = ['script_id', 'script_name','status_id', 'script_status_comments', 'request','script_version', 'script_repo','script_branch','testbeds',]
        widgets = {
           'status_id': forms.HiddenInput(),
           }
        help_texts = {
           'script_id': 'Provide unique script id, only digits are allowed. * Mandatory',
           'status_id': 'Select one option out of following - Submitted, New, Production, Decommissioned. * Mandatory',
           }
        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
