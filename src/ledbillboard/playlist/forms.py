from django import forms
from fancy_cronfield.widgets import CronWidget
from ledbillboard.playlist.models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('playlist', 'timing')
        widgets = {
            'timing': CronWidget(
                attrs={'class': 'special'},
                options={'use_gentle_select': False}
            ),
        }
