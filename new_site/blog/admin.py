from django.contrib import admin
from .models import Post


class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Post, AdminPost)
