from django import forms
from django.forms import ModelForm
from core.models import SignUp, Contact, Block

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ['name','pagename','email','password',]

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'text']

class DevForm(ModelForm):
    class Meta:
        model = Block
        fields = ['data', 'hp_user', 'temp']
