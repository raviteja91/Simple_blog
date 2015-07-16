from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=42)
    text = models.TextField()
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name



