from django.db import models
from django.conf import settings
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    body = models.TextField()
    postdate = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def clean(self):
        self.name = slef.name.lower()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse('tag_posts', args=[str(self.name)])