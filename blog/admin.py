from django.contrib import admin

from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'slug', 'author', 'publish', 'status')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title', )}
	raw_id_fields = ('author', )
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

	list_display = ('name', 'post', 'body', 'active', 'created')
	search_fields = ('body', 'name')
