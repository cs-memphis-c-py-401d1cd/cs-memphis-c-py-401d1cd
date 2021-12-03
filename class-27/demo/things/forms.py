# Contain all our model based forms
from django.forms import ModelForm
# know what model we want to use to generate forms before we can use the cool built in functionality
from .models import Thing

# Define a basic form
# class ThingForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=128)
#     rating = forms.IntegerField(label='Rating')

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'rating', 'reviewer']