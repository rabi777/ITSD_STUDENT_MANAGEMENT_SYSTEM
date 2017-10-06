from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^topic/$', views.CreateTopic.as_view(), name = 'register_topic'),
    url(r'^topic/list/$', views.ListTopic.as_view(), name = 'topic_list'),
    url(r'topic/edit/(?P<pk>[0-9]+)/$', views.UpdateTopic.as_view(), name = 'update_topic'),
    url(r'topic/details/(?P<pk>[0-9]+)/$', views.TopicDetails.as_view(), name = 'topic_details'),
    url(r'^course/$', views.CreateCourse.as_view(), name = 'create_course'),
    url(r'^course/list/$', views.ListCourse.as_view(), name = 'course_list'),
    url(r'^course/edit/(?P<pk>[0-9]+)/$', views.UpdateCourse.as_view(), name = 'update_course'),
    url(r'^class/$', views.CreateClass.as_view(), name = 'create_class'),
    url(r'^class/list/$', views.ListClass.as_view(), name = 'class_list'),
    url(r'^class/edit/(?P<pk>[0-9]+)/$', views.UpdateClass.as_view(), name = 'update_class'),
]
