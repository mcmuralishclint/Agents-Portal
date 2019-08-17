from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserDetail(models.Model):
	USER_CHOICES = (
        ('A', 'Agent'),
        ('S', 'Student'),)


	image = models.ImageField(upload_to='profile_pic/', blank=False)
	user_type = models.CharField(max_length=20, choices=USER_CHOICES, default="S")
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_detail")
	country = models.CharField(max_length=100, default="China")
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('user:profile', kwargs={'id': self.id
        })

