from django.urls import path

from users.views import *


urlpatterns = [
    path('',home_page,name='home'),
    path('add_student/',add_student,name="add_student"),
    path('download_pdf/', download_students_pdf, name='download_pdf'),
]