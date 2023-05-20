from django import forms


class MemoForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(label="Content", widget=forms.Textarea, max_length=300)
    created_at = forms.DateTimeField(label="Created at", widget=forms.SelectDateWidget)
