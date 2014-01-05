from django.contrib import admin
from article.models import Article
from article.models import Comment

# Register your models here.

# class ArticleAdmin()
admin.site.register(Article)

class CommentAdmin(admin.ModelAdmin):
	display_fields = ["post","author","created"]

admin.site.register(Comment,CommentAdmin)