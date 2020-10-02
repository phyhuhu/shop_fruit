from django import forms
from django.forms import ModelForm, DateInput, ChoiceField
from .models import CreateQModel, CreateTaskModel

class QForm(ModelForm):
  class Meta:
    model = CreateQModel
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    # fields = '__all__'
    fields = ['task_name', 'fruit', 'quantity', 'repeats', 'schedule_type', 'schedule_quantity', 'start_time']

  def __init__(self, *args, **kwargs):
    super(QForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class TaskForm(ModelForm):
  class Meta:
    model = CreateTaskModel
    fields = ['fruit', 'quantity']