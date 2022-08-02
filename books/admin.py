from django.contrib import admin
from . import models 

@admin.register(models.Book)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}