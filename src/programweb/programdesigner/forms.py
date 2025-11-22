from django import forms
from .models import ProgramTalk, Event


class ProgramTalkAdminForm(forms.ModelForm):
    class Meta:
        model = ProgramTalk  # Replace MyModel with your actual model name
        fields = '__all__'

        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
            'end_time': forms.TimeInput(format='%H:%M')
        }

    # Customize the TimeField
    start_time = forms.TimeField(
        input_formats=['%H:%M'],  # Accepts only HH:MM format
        widget=forms.TimeInput(format='%H:%M') # Displays HH:MM in the widget
    )

    end_time = forms.TimeField(
        input_formats=['%H:%M'],  # Accepts only HH:MM format
        widget=forms.TimeInput(format='%H:%M') # Displays HH:MM in the widget
    )

