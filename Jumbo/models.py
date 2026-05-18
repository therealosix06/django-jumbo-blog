from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',
                       kwargs={'pk': self.pk})
    


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    parent=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE, related_name='replies')
    date_posted=models.DateTimeField(default=timezone.now)
    