from django.contrib import admin
from .models import Post, Comment


class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    pass

admin.site.register(Comment, AdminComment)
