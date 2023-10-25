from django.db import models
from blog.apps.users.models import CustomUser 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag", related_name="tags", verbose_name="Tags", blank=True, null=True, default='general')

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

