from django.contrib import admin
from .models import Article, Category, Subject, ArticleComment,SubjectComment, CategoryComment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject_name','created_date','published_date', 'slug']
    list_display_links = ['title']
    list_filter = ['published_date']
    search_fields = ['title','text']
    list_editable = ['subject_name']

    class Meta:
        model=Article


# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryComment)
admin.site.register(Subject)
admin.site.register(SubjectComment)
admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleComment)
