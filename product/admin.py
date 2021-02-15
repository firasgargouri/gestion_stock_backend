from django.contrib import admin
from . import models


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'subCategory', 'description', 'prix')


@admin.register(models.SubCategory)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'subCategory', 'category')


admin.site.register(models.Category)
# admin.site.register(models.SubCategory)
