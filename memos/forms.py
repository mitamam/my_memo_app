from django import forms


class MemoForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control mb-2'},
            format="%Y-%m-%d %H:%M"
        )
    )
