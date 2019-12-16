from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from markdown import markdown

from blog.models import Post

register = template.Library()


@register.simple_tag
def total_posts():
	return Post.objects.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Post.objects.order_by('-created')[:count]
	return {'latest_posts': latest_posts}


@register.simple_tag
def most_commented_posts(count=5):
	return Post.objects.annotate(
		total_comments=Count('comments')
	).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown(text))