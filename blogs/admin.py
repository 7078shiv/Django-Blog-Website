from django.contrib import admin
from .models import Category, Post


# Register your models here.

# for configuration of category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag_cat', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)
    list_per_page = 5


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag_post', 'title', 'url', 'cat')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    class Media:
        js = ('https://cdn.tiny.cloud/1/xxv081hst5rq0aour0vvkthckwyhkl7m52cgjxpaqk3g6296/tinymce/6/tinymce.min.js',
              'JS/script.js')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
