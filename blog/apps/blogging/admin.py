from django.contrib import admin
from .models import Post, Tag, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('published', 'updated')

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('published', 'updated')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)