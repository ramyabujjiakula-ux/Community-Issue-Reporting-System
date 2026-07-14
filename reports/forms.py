from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Issue, Reply


# Form for submitting issues
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'category', 'custom_category', 'photo']
        widgets = {
            'custom_category': forms.TextInput(
                attrs={'placeholder': 'Specify your category if Other'}
            ),
        }


# Custom signup form
class CustomSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]
        help_texts = {k: "" for k in fields}
        widgets = {
            'password1': forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),
            'password2': forms.PasswordInput(
                attrs={'placeholder': 'Confirm Password'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""


# Admin Reply Form
class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['message']

        widgets = {
            'message': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'form-control',
                    'placeholder': 'Type your reply...'
                }
            )
        }