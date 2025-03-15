from django.contrib import admin

from .models import *

class NewFan(admin.ModelAdmin):
    list_display = ('f_name',)
    search_fields = ('f_name',)

admin.site.register(Fanlar,NewFan)


class NewStudent(admin.ModelAdmin):
    list_display = ('first_name','last_name','tel_num','fan','email')
    search_fields = ('first_name','tel_num')


admin.site.register(Student,NewStudent)