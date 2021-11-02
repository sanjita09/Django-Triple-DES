from django import forms

class EncryptForm(forms.Form):
    title=forms.CharField(max_length=250)
    image=forms.FileField()
    key=forms.CharField()

class DecryptForm(forms.Form):
    title=forms.CharField(max_length=250)
    Encoded_file=forms.FileField()
    key=forms.CharField()
    
    