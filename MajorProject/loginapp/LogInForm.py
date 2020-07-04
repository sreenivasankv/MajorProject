from django import forms
from .models import user, UserBlog

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        #fields = '__all__'
        fields = ('email','password')

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        #fields = ('email','password')


class BlogForm(forms.ModelForm):
    class Meta:
        model = UserBlog
        fields = '__all__'
        #fields = ('blogheader','blog')