from django.contrib import admin

from.models import Task

# Override some admin settings
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_complete', 'updated_at')
    search_fields = ('task',)

# Register your models here.
admin.site.register(Task, TaskAdmin)