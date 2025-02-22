from django.db import models

# Create your models here.

class Contact(models.Model):
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	first_line_address = models.CharField(max_length=250)
	post_code = models.CharField(max_length=20)
	contact_number = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.first_name} {self.last_name} ({self.email})"
		