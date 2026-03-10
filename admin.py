from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('created_date', 'published_date', 'author')
    search_fields = ('title', 'text')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date', 'author')
    list_editable = ('approved_comment',)
    search_fields = ('author', 'text')

admin.site.site_header = 'Blog Project administration'
admin.site.index_title = 'Blog Dashboard'
admin.site.site_title = 'Blog Admin'


# Register your models here.

