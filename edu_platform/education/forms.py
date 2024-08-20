from django import forms

class FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your feedback here'}), label='')
