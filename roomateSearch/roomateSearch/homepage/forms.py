from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from homepage.models import RoomateUser
import re

ACTION_CHOICES= [
    ('login', 'Login'),
    ('create account', 'Create Account'),
    ]
QUESTION_CHOICES= [
    ('always','Always'),
    ('most of the time','Most of the Time'),
    ('sometimes', 'Sometimes'),
    ('never', 'Never'),
]
input_regex = re.compile(r'/^[\w_\.\-]+$/')
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password')
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    """def clean_username(self):
        data = self.cleaned_data['username']
        #check username for invalid characters
        if(input_regex.match(data) is None):
            data="invalid"
        return data
    def clean_password(self):
        data = self.cleaned_data['password']
        #check password for invalid characters
        if(input_regex.match(data) is None):
            data="invalid"
        return data"""
        
class RoomateUserForm(forms.ModelForm):
    answer_one = forms.CharField(label='Do you prefer to go to sleep late?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_two = forms.CharField(label='Do you prefer to wake up early?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_three = forms.CharField(label='Do you prefer to keep your room cold?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_four = forms.CharField(label='Do you prefer to go study in your room?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    answer_five = forms.CharField(label='Do you prefer to listen to music in the room?',widget=forms.RadioSelect(choices=QUESTION_CHOICES))
    bio = forms.CharField(label='Enter a short bio about yourself up to 500 characters:', widget=forms.Textarea, required=False)
    image = forms.ImageField(label='Profile Picture:', required=False)
    class Meta:
        model = RoomateUser
        fields = ('answer_one', 'answer_two', 'answer_three', 'answer_four', 'answer_five', 'bio', 'image')
    
class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class chooseForm(forms.Form):
    action = forms.CharField(label='Action:', widget=forms.RadioSelect(choices=ACTION_CHOICES))
    