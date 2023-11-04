from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return(f'{ self.title } by { self.username }.')
    
class LoginUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return(f'{ self.username }')
    
class Comment(models.Model):
    content = models.CharField(max_length=2000)
    username = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return(f'{ self.content }')