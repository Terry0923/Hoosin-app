
from django import forms
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comment
from django.core.validators import EmailValidator

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def clean_email(self):
        submitted_data = self.cleaned_data['email']
        ALLOWED_DOMAINS = "virginia.edu"
        domain = submitted_data.split('@')[1]
        if domain not in ALLOWED_DOMAINS:
            raise forms.ValidationError(
                f'Domain name must be "virginia.edu"'
            )
        return submitted_data
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'status', 'year','major','school', 'bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'body', 'type']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

#for testing purposes
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password','first_name')
