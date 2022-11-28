from django import forms
from .models import SlipModel


class SlipForm(forms.ModelForm):
    class Meta:
        model = SlipModel
        # fields = "__all__"
        exclude = ['slip_id']