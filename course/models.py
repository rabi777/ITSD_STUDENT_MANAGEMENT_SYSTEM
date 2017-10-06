# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

#topic model
class Topic(models.Model):
    topic_name = models.CharField(max_length=20)
    details = models.TextField()

    def get_absolute_url(self):
        return reverse('course:topic_list')

    def __str__(self):
        return self.topic_name



#course model
class Course(models.Model):
    topic_name = models.ForeignKey(Topic)
    course_name = models.CharField(max_length=50)
    category_name = models.CharField(max_length = 20)
    course_amount = models.CharField(max_length = 20)
    teacher_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('course:course_list')

    def __str__(self):
        return self.course_name



#class model
class Class(models.Model):
    topic_name = models.ForeignKey(Topic)
    course_name = models.ForeignKey(Course)
    start_date = models.DateField()
    end_date = models.DateField()

    def get_absolute_url(self):
        return reverse('course:class_list')



