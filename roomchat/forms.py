
from django import forms
from django.contrib.auth.models import User
from .models import Room,Roomchat
from django.contrib.auth.forms import UserCreationForm

class NewRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name','logo']
        exclude = ['admin']

class NewChatForm(forms.ModelForm):
    class Meta:
        model = Roomchat
        exclude=["author","room"]
        fields = '__all__'


class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)