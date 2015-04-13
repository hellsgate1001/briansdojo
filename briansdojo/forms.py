from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['sender'].widget.attrs['placeholder'] = self.fields['sender'].label
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['message'].widget.attrs['placeholder'] = self.fields['message'].label

    class Meta:
        model = Contact
