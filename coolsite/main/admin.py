from django.contrib import admin

from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'date_create')


admin.site.register(Task, TaskAdmin)
admin.site.register(Categories)
