from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        'class':'form-control',
        'placeholder':'email@domain.com',
        'aria-describedby':'emailHelp'
        }
    ))

    subject = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'email subject',
        'aria-describedby':'texthelp'
        }
    ))

    message = forms.CharField(widget=forms.Textarea(
        attrs={
        'class':'form-control',
        'placeholder':'Your message',
        'aria-describedby':'texthelp'
        }
    ))

    class Meta:
        model = Contact
        fields = '__all__'