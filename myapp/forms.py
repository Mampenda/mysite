from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)  # Label is the text that shows before the input-box
    check = forms.BooleanField()  # Boolean check button