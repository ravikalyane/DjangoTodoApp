from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Task, TaskAdmin)
