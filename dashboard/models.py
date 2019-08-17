from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import UserDetail
# Create your models here.

class University(models.Model):
	university = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	tuition = models.IntegerField(default=0)
	accomodation = models.IntegerField(default=0)
	about = models.TextField(default="")
	logo = models.ImageField(upload_to='logo/', blank=False)

	def __str__(self):
		return self.university
		
class Scholarship(models.Model):
	SCHOLARSHIP_CHOICES = (
        ('F', 'Full Scholarship'),
        ('P', 'Partial Scholarship'),
    )



	university = models.ForeignKey(University,on_delete=models.CASCADE)
	tuition_after_schol = models.IntegerField(default=0)
	accomodation_after_schol = models.IntegerField(default=0)
	stipend = models.IntegerField(default=0)
	agent = models.ForeignKey(User, on_delete = models.CASCADE)
	schol_type = models.CharField(max_length=20, choices=SCHOLARSHIP_CHOICES, default="P")
	service_charge = models.IntegerField(default=500)

	def __str__(self):
		return str(self.university) + " - " + str(self.agent)

	def get_absolute_url(self):
		return reverse('dashboard:scholarship_view', kwargs={'id': self.id
        })


