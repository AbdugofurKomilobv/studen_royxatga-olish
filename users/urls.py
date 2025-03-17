from django.urls import path

from users.views import *


urlpatterns = [
    path('',home_page,name='home'),
    path('add_student/',add_student,name="add_student"),
    path('download_pdf/', download_students_pdf, name='download_pdf'),
    path('update_stu/<int:student_id>/',udate_student,name='update_stu'),
    path('student_v/<int:student_id>/',view_full,name='student_v'),
    path('delete_student/<int:student_id>/',delete_student,name='delete_student'),
]