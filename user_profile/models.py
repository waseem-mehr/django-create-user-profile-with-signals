from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  bio=models.TextField(max_length=50,null=True)
  age=models.IntegerField(null=True)
  education=models.CharField(max_length=20,null=True)
  address=models.CharField(max_length=50,null=True)
  image=models.ImageField(upload_to='media/',default='user_profile/profile.jpg')
  def __str__(self):
    return self.user.username+" profile "
