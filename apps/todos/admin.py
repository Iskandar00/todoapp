from django.contrib import admin

from apps.todos.models import Todo



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('categories', 'title', 'text', 'done', 'done_at', 'start_date', 'days', 'created_at',)
    list_display_links = list_display