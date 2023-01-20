from django.contrib import admin
from .models import Todo, Registration


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'status', 'priority', 'created_at']
    list_filter = ['author', 'status', 'priority']
    search_fields = ['title', 'author__username']
    date_hierarchy = 'created_at'


admin.site.register(Todo, TodoAdmin)
admin.site.register(Registration)