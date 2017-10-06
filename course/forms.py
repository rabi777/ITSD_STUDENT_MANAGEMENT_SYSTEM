from django import forms
from .models import Topic, Course, Class


#topic form
class TopicForm(forms.ModelForm):
    topic_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))

    class Meta:
        model = Topic
        fields = ['topic_name','details']


#course form
class CourseForm(forms.ModelForm):

    CHOICES = (('', 'select course'), ('Python', 'Python'), ('Java Script', 'Java Script'),
               ('Web Design', 'Web Design'), ('Php', 'Php'),
               ('Networking', 'Networking'), ('Graphics', 'Graphics'),
               ('Wordpress', 'Wordpress'), ('SEO', 'SEO'),
               ('IT Manager', 'IT Manager'), )

    CHOICESS = (('', 'select category'), ('Basic', 'Basic'), ('Intermediate', 'Intermediate'),
               ('Advanced', 'Advanced'),)

    topic_name = forms.ModelChoiceField(queryset=Topic.objects.all(), widget=forms.Select(attrs={'class' : 'form-control'}))
    course_name = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))
    category_name = forms.ChoiceField(choices=CHOICESS, widget=forms.Select(attrs={'class': 'form-control'}))
    # course_amount = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    teacher_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Course
        fields = ['topic_name', 'course_name', 'category_name', 'teacher_name', 'contact_number']



# class form
class ClassForm(forms.ModelForm):
    CHOICES = (('', 'select your course'), ('Basic', 'Basic'), ('Intermediate', 'Intermediate'),
               ('Advanced', 'Advanced'),)

    topic_name = forms.ModelChoiceField(queryset = Topic.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    course_name = forms.ModelChoiceField(queryset = Course.objects.all(), widget=forms.Select(attrs = {'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.widgets.DateInput(format="%d %B, %Y",attrs = {'class': 'form-control','type' : 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(format="%d %B, %Y", attrs = {'class': 'form-control','type' : 'date'}))

    class Meta:
        model = Class
        fields = ['topic_name', 'course_name', 'start_date', 'end_date']
