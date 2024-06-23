from django.contrib import admin

from task.models import Task, User


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Task,TaskAdmin)

admin.site.register(User,UserAdmin)




