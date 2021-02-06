from django.contrib import admin
from .models import Category,Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published','post__categories')
    ordering=('author','published')
    search_fields=('title','context','author__username','categories__name')
    date_hierarchy='published'
    list_filter=('author__username','categories__name')
    
    def post__categories(self, obj):

        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post__categories.short_description="Categorias"

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
