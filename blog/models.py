from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse


class Post(models.Model):
    role=models.CharField(max_length=100)
    skills=models.CharField(max_length=50)
    domain=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    jd=models.TextField()
    opening=models.IntegerField()
    date_posted=models.DateTimeField(default=timezone.now)
    last_date=models.DateField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role} by {self.author.name}"
    def get_absolute_url(self):
        # redirect is not used because we want view to handle it
        # reverse return the url in the form of string required by view to redirect  
        return reverse ('hiring-detail',kwargs={'pk':self.pk})
