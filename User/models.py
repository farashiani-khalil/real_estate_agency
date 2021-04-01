from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(blank = True)
    created = models.DateTimeField(default = timezone.now)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    number = models.IntegerField(default=0)
    code_agency = models.IntegerField(null=True, blank=True, default=0)
