from django.contrib import admin

from apps.categories.models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ['name']}
    list_display_links = list_display
