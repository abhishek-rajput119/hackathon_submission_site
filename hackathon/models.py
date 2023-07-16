from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Hackathon(models.Model):
    IMAGE = 0
    FILE = 1
    LINK = 2

    TYPE_OF_SUBMISSION = (
        (IMAGE, "image"),
        (FILE, "file"),
        (LINK, "link"),
    )
    user_id = models.IntegerField()
    type_of_submission = models.PositiveIntegerField(choices=TYPE_OF_SUBMISSION)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length= 200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)
    reward = models.PositiveIntegerField()
    background_image = models.TextField(null=True)
    hackathon_image = models.TextField(null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    
class Submission(models.Model):
    hackathon_id= models.IntegerField()
    user_id= models.IntegerField()
    summary= models.TextField()
    title = models.CharField(max_length=100,null=True)
    link = models.TextField()
    file = models.TextField()
    

class Registration(models.Model):
    user_id = models.IntegerField()
    hackathon_id = models.IntegerField()