from django import forms

class MeetingCreation(forms.Form):
    """
    Define the Meeting registration fields.
    """
    name = forms.CharField(label='Meeting Name', max_length=24)
    date = forms.SelectDateWidget()
    file = forms.FileField()