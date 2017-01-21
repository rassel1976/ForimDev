from django.contrib import admin

# Register your models here.
from forum.models import Post, Comment

class PostInLine(admin.StackedInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin):
    feilda = ['post_name','post_text','post_time']
    inlines = [PostInLine]
    list_filter = ['post_time']

admin.site.register(Post, PostAdmin)