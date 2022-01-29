from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label='18')
    required_css_class = "field"
    error_css_class = "error"



