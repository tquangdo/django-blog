from django import forms


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'contentCName'}))
    cc = forms.BooleanField(required=False)
