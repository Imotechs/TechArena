from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from mainapp.models import Software
from .models import Student

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args,**kwargs)
        for fieldname in ['username','email','password1', 'password2']:
            self.fields[fieldname].help_text = None


# class StudentRegisterForm(UserCreationForm):  
#     model = Student  
#     class Meta:
#         fields = ['username','surname','last_name','midle_name'] 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    #First_Name = forms.CharField(max_length=50, required= False)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name'] 
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args,**kwargs)
        for fieldname in ['username','email','first_name','last_name']:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    # image = forms.ImageField(required=False)
    class Meta:
        model = Student
        fields = ['image']
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args,**kwargs)
        for fieldname in ['image']:
            self.fields[fieldname].help_text = None


class studentRegistrationForm(forms.ModelForm):
    software = forms.ModelMultipleChoiceField(queryset=Software.objects.all(),
         widget = forms.CheckboxSelectMultiple, required = False)
    class Meta:
        model = Student
        fields = ['software']

    def __init__(self, *args, **kwargs):
        super(studentRegistrationForm, self).__init__(*args,**kwargs)
        for fieldname in ['software']:
            self.fields[fieldname].help_text = None