from django.contrib import admin
from .models import BlogPost
from .models import Tag

admin.site.register(BlogPost)
admin.site.register(Tag)