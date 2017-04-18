# -*- coding: utf-8 -*-
from django import forms
from fancy_cronfield.widgets import CronWidget
from ledbillboard.playlist.models import Playlist


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('media', 'board', 'timing')
        widgets = {
            'timing': CronWidget(
                attrs={'class': 'special'},
                options={'use_gentle_select': True}
            ),
        }
