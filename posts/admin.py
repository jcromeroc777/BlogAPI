from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)