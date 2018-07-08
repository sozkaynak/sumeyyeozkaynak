from django.contrib import admin
from .models import Post, Category, Subject

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject_name','created_date','published_date']
    list_display_links = ['title']
    list_filter = ['published_date']
    search_fields = ['title', 'text']
    list_editable = ['subject_name']

    class Meta:
        model=Post


# Register your models here.
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Post, PostAdmin)