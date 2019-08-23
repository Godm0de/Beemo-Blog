from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'email', 'placeholder' : 'Enter your email ...', 'id' : 'emailInput'}) ,required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'text', 'placeholder' : 'Enter the subject ...', 'id' : 'subjectInput'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'type' : 'text', 'placeholder' : 'Write your message...', 'id' : 'msgInput'}), required=True)
