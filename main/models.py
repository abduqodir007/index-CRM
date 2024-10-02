from django.db import models
from django_resized import ResizedImageField



class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol'), ('Boshqa', 'Boshqa')])
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    region = models.CharField(max_length=50)
    city_or_district = models.CharField(max_length=50)
    profile_image = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='profiles/')

    def __str__(self):
        return f"{self.name} {self.surname}"
        