from django import forms


class DownVoteForm(forms.Form):
    url = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter URL here.'}), label='url')
