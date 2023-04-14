from django import forms

class NameForm(forms.Form):
    Number1 =forms.IntegerField(label='NUMBER1')
    Number2=forms.IntegerField(label='NUMBER2')