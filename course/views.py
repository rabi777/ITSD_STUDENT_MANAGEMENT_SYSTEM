# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, View
from django.views import generic
from .models import Topic, Course, Class
from django.utils import timezone
from .forms import TopicForm, CourseForm, ClassForm
from django.contrib.messages.views import SuccessMessageMixin


#index view
class Index(View):
    template_name = "dashboard/dashboard.html"
    def get(self, request):
        return render(request, self.template_name)


#create topic
class CreateTopic(CreateView):
    template_name = 'forms/topic_form.html'
    def get(self, request, pk=None):
        form = TopicForm()
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })

    def post(self, request):
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/itsd/topic/list/')
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })


#List Topic
class ListTopic(generic.ListView):
    template_name = 'tables/topic_table.html'
    def get_queryset(self):
        return Topic.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListTopic, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#update topic
class UpdateTopic(SuccessMessageMixin, UpdateView):
    model = Topic
    template_name = 'forms/topic_edit.html'
    form_class = TopicForm
    success_message = "Topic updated successfully!!!"

    def get_context_data(self, **kwargs):
        context = super(UpdateTopic, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#topic details
class TopicDetails(generic.DetailView):
    template_name = 'tables/topic_details.html'
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetails, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#create course
class CreateCourse(CreateView):
    template_name = 'forms/course_form.html'

    def get(self, request):
        form = CourseForm
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/itsd/course/list/')
        return render(request, self.template_name)


#course list view
class ListCourse(generic.ListView):
    template_name = "tables/course_table.html"
    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListCourse, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#course update view
class UpdateCourse(SuccessMessageMixin, UpdateView):
    model = Course
    template_name = 'forms/course_edit.html'
    form_class = CourseForm
    success_message = "Course updated successfully!!!"

    def get_context_data(self, **kwargs):
        context = super(UpdateCourse, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



#create class
class CreateClass(CreateView):
    template_name = 'forms/class_form.html'

    def get(self, request):
        form = ClassForm
        context = timezone.now()
        return render(request, self.template_name, {
            'form' : form,
            'now' : context
        })

    def post(self, request):
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/itsd/class/list/')
        return render(request, self.template_name, {
            'form' : form
        })


#update class
class UpdateClass(SuccessMessageMixin, UpdateView):
    model = Class
    template_name = 'forms/class_form.html'
    form_class = ClassForm
    success_message = "Class updated successfully"

    def get_context_data(self, **kwargs):
        context = super(UpdateClass, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#Class List
class ListClass(generic.ListView):
    template_name = 'tables/class_table.html'
    def get_queryset(self):
        return Class.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListClass, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
