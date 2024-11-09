from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# Define blood group choices
BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class donors(models.Model):
    full_name = models.CharField(max_length=255,verbose_name=_("Full Name"))
    email = models.EmailField(unique=True,verbose_name=_("Email"))
    contact_number = models.CharField(max_length=15,verbose_name=_("Contact Number"))
    date_of_birth = models.DateField(verbose_name=_("Date of birth"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name=_("Gender"))
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,verbose_name=_("Blood Group"))
    organ_to_donate = models.CharField(max_length=255,verbose_name=_("Organ to donate"))
    address = models.TextField(verbose_name=_("Address"))


class recipients(models.Model):
    full_name = models.CharField(max_length=255,verbose_name=_("Full Name"))
    email = models.EmailField(unique=True,verbose_name=_("Email"))
    contact_number = models.CharField(max_length=15,verbose_name=_("Contact Number"))
    date_of_birth = models.DateField(verbose_name=_("Date of birth"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name=_("Gender"))
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,verbose_name=_("Blood Group"))
    organ_needed = models.CharField(max_length=255,verbose_name=_("Organ Needed"))
    address = models.TextField(verbose_name=_("Address"))

    def __str__(self):
        return self.full_name
