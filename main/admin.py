from django.contrib import admin

from main import models

@admin.register(models.Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", ) 


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", ) 


@admin.register(models.ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ("title", ) 


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", ) 