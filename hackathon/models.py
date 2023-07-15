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
    user_id = models.IntegerField()
    title = models.CharField(max_length=40)
    description = models.TextField(max_length= 200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    active = models.DateTimeField()
    reward = models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

class Submission(models.Model):
    IMAGE = 0
    FILE = 1
    LINK = 2

    TYPE_OF_SUBMISSION = (
        (IMAGE, "image"),
        (FILE, "file"),
        (LINK, "link"),
    )
    hackathon_id = models.IntegerField()
    user_id = models.IntegerField()
    summary = models.TextField()
    type_of_submission = models.PositiveIntegerField(choices=TYPE_OF_SUBMISSION)

