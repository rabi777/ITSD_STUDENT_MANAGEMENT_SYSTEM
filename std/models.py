from django.db import models
from course.models import Course
from django.core.urlresolvers import reverse



#interested student registration form
class RegisterForInterestStudent(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    ocupation = models.CharField(max_length=50)
    course_name = models.ForeignKey(Course)
    institute_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.course_name)


#student registraton form
class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=50)
    current_address = models.CharField(max_length=50)
    ocupation = models.CharField(max_length=50)
    academic_qualification = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    id_no = models.CharField(max_length=50)
    course_name = models.ForeignKey(Course)
    skill = models.CharField(max_length=50)
    machine = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


    def get_absolute_url(self):
        return reverse('std:register_table')
