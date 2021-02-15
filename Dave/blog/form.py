from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("Name","Email","Body")

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeNewsletter
        fields = ("subscriberemail",)

class LetsConnectForm(forms.ModelForm):
    class Meta:
        model = LetsConnect
        fields = ("firstname","lastname","lc_email","lc_phone_no","lc_message")