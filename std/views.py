from django.shortcuts import render
from django import forms
from django.views.generic.edit import View, UpdateView
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import RegisterForm, InterestedStudentForm
from .models import Register, RegisterForInterestStudent
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin


#index view
class Index(View):
    template_name = "dashboard/dashboard.html"
    def get(self, request):
        return render(request, self.template_name)


#Interested student
class InterestedStudentRegisterView(View):
    template_name = 'forms/interested_students.html'
    def get(self, request):
        form = InterestedStudentForm
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })

    def post(self, request):
        form = InterestedStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/itsd/interested_student_table/')
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })


#Interested Student Table
class InterestedStudentTableView(View):
    template_name = 'tables/interested_students_table.html'
    def get(self, request):
        student = RegisterForInterestStudent.objects.all()
        context = timezone.now()
        return render(request, self.template_name, {
            'student' : student,
            'now' : context
        })


#get data form interested student
class GetDataFromInterestedStudent(View):
    template_name = "forms/register_student.html"
    def get(self, request, id):
        student = RegisterForInterestStudent.objects.get(id = id)
        form = RegisterForm(initial=[student])
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })



#itsd student registration
class RegisterView(View):
    template_name = 'forms/register_student.html'
    def get(self, request):
        form = RegisterForm
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/itsd/student_table/')
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })


#itsd student table
class RegisterStudentTableView(View):
    template_name = 'tables/register_student_table.html'
    def get(self, request):
        student = Register.objects.all()
        context = timezone.now()
        return render(request, self.template_name, {
            'students' : student,
            'now' : context
        })


#itsd student detail view
class RegisterStudentDetailsView(generic.DetailView):
    template_name = 'tables/student_details_table.html'
    model = Register

    def get_context_data(self, **kwargs):
        context = super(RegisterStudentDetailsView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#itsd student update view
class UpdateRegisterStudent(SuccessMessageMixin, UpdateView):
    model = Register
    template_name = 'forms/register_student_edit.html'
    form_class = RegisterForm
    success_message = 'Registration Updated successfully!!!!'

    def get_context_data(self, **kwargs):
        context = super(UpdateRegisterStudent, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
