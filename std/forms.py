from django import forms
from .models import Register, RegisterForInterestStudent
from course.models import Course


class InterestedStudentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ocupation = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_name = forms.ModelChoiceField(queryset= Course.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    institute_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RegisterForInterestStudent
        fields = ['name','phone_no','ocupation','course_name','institute_name','address']



class RegisterForm(forms.ModelForm):

    CHOICES=[
         ('computer basic','computer basic'),('none','None'),]

    CHOICESS=[
         ('Laptop','Laptop'),('Desktop','Desktop'),('none','None'),]

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    father_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    permanent_address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ocupation = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    academic_qualification = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    institute_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(format="%d %B, %Y",attrs = {'class': 'form-control','type' : 'date'}))
    phone_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': False}))
    course_name = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    skill = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs = {'class' : 'radio-inline'}))
    machine = forms.ChoiceField(choices=CHOICESS, widget=forms.RadioSelect(attrs = {'class' : 'radio-inline'}))


    class Meta:
        model = Register
        fields = ['name','email','father_name',
                  'mother_name','permanent_address',
                  'current_address','ocupation','academic_qualification',
                  'institute_name','date_of_birth','phone_no','id_no',
                  'course_name','skill','machine']
