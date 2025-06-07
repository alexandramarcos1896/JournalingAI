from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'notes_main'
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'profile_main'


