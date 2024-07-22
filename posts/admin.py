from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'content', 'is_private')


admin.site.register(Post, PostAdmin)
