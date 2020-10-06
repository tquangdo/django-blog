from django.contrib import admin
from .models import Post, Comment, Choice

# from .models import Post, Comment, Choice, CustomUser


# StackedInline OR TabularInline
class CommentInline(admin.TabularInline):
    model = Comment


class PostDoTQ(admin.ModelAdmin):
    list_display = ['title', 'body', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]


admin.site.register(Post, PostDoTQ)
admin.site.register(Choice)
# admin.site.register(CustomUser)
