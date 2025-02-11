from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class":"form-control comment-form-name w-25","placeholder": "Your name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class":"form-control comment-form-body","placeholder":"Leave a comment","rows":5}
        )
    )

