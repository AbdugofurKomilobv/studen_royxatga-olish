import re
from django import forms

from users.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
          model = Student
          fields = ['first_name','last_name','tel_num','fan','email']


