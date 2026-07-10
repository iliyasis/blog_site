from django import forms

class contactus_form(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام و نام خانوادگی'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'ایمیل'}))
    subject = forms.CharField(label='subject', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'موضوع'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'پیام شما'}))