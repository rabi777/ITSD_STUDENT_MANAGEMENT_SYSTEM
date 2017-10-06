from django.conf.urls import url
from . import views
from .views import Index, RegisterView, RegisterStudentTableView, InterestedStudentRegisterView, InterestedStudentTableView


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^interested_student/$', InterestedStudentRegisterView.as_view(), name = 'interest_student_form' ),
    url(r'^interested_student_table/$', InterestedStudentTableView.as_view(), name='interested_student_table'),
    url(r'^register/$', RegisterView.as_view(), name ='register_form'),
    url(r'^student_table/$', RegisterStudentTableView.as_view(), name ='register_table'),
    url(r'^student/details/(?P<pk>[0-9]+)/$', views.RegisterStudentDetailsView.as_view(), name ='student_detail_view'),
    url(r'^student/edit/(?P<pk>[0-9]+)/$', views.UpdateRegisterStudent.as_view(), name ='student_update_view'),
]
