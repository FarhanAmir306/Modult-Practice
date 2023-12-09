from django import forms 
from .import models

class TaskForm(forms.ModelForm):
    class Meta:
        model=models.TaskModel
        fields='__all__'
        widgets = {
            'Task_Assign_Date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        

        