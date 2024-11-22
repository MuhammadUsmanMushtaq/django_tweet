from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Apply Tailwind classes to TweetForm fields
    #     self.fields['text'].widget.attrs.update({
    #         'class': 'border-cyan-600 rounded-lg shadow-sm focus:ring-cyan-600 focus:border-cyan-600 block w-[360px] p-2.5 mb-2'
    #     })
    #     self.fields['photo'].widget.attrs.update({
    #         'class': 'border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5'
    #     })

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Apply Tailwind classes to TweetForm fields
    #     self.fields['username'].widget.attrs.update({
    #         'class': 'border-cyan-600 rounded-lg shadow-sm focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5 mb-2'
    #     })
    #     self.fields['email'].widget.attrs.update({
    #         'class': 'border-cyan-600 rounded-lg shadow-sm focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5 mb-2'
    #     })
    #     self.fields['password1'].widget.attrs.update({
    #         'class': 'border-cyan-600 rounded-lg shadow-sm focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5 mb-2'
    #     })
    #     self.fields['password2'].widget.attrs.update({
    #         'class': 'border-cyan-600 rounded-lg shadow-sm focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5 mb-2'
    #     })

