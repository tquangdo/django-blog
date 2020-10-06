from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    # "post" & "author" là auto created fields thì cho vô def()
    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        cmt = super().save(commit=False)
        cmt.post = self.post
        cmt.author = self.author
        cmt.save()

    # "body" KO là auto created fields thì cho vô class Meta
    class Meta:
        model = Comment
        fields = ["body"]
        # fields = ("post", "author", "body")
        # widgets = {'body': forms.TextField(attrs={'class': 'bodyCName'})}
