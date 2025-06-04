from django.db import models

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)

class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
