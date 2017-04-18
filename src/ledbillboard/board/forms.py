from django import forms
from ledbillboard.board.models import Board
from django.utils.translation import ugettext_lazy as _


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('user', 'name', 'slug', 'lat', 'lon')

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        if user and not user.is_lessor:
            raise forms.ValidationError(_('User has to be a lessor.'))
