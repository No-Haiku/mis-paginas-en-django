from django.contrib import admin
from .models import Category,Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Post, PostAdmin)
