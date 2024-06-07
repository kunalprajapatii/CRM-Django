from django.db import models

# Create your models here.

class customer(models.Model):
    creation_data = models.DateTimeField(auto_now_add=True)  # Automatically set to the current
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    

    def __str__(self):
        return self.first_name + "  " + self.last_name