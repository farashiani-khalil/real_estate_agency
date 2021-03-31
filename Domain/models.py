from django.db import models
from User.models import User
from django.utils import timezone

class Image(models.Model):
    image1 = models.ImageField(blank = True)
    image2 = models.ImageField(blank = True)
    image3 = models.ImageField(blank = True)

class Rent(models.Model):
    COUNTRY_CHOICES = [
        ('IR', 'Iran'),
    ]
    CITY_CHOICES = [
        ('TEH', 'Tehran'),
        ('MAS', 'Mashhad'),
        ('ESF', 'Esfehan'),
    ]
    ZONE_CHOICES = [
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),
        ('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
        ('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),
        ('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),
    ]
    TYPE_HOUSE = [
        ('APA', 'apartment'),
        ('VIL', 'villa'),
        ('LAN', 'land'),
    ]
    USE = [
        ('RES', 'residential'),
        ('COM', 'commercial'),
    ]
    country = models.CharField(choices=COUNTRY_CHOICES, default='IR', max_length=50)
    city = models.CharField(choices=CITY_CHOICES, default='TEH', max_length=50)
    zone = models.CharField(choices=ZONE_CHOICES, default='1', max_length=50)
    mortgage = models.DecimalField(default=0, decimal_places=2, max_digits=100000000000)
    rent = models.DecimalField(decimal_places=2, max_digits=100000000000)
    area = models.DecimalField(decimal_places=2, max_digits=1000000)
    number_of_rooms = models.DecimalField(decimal_places=2, max_digits=7)
    age_of_house = models.DecimalField(decimal_places=2, max_digits=100)
    parking = models.DecimalField(decimal_places=2, max_digits=100)
    warehouse = models.DecimalField(decimal_places=2, max_digits=1000)
    elevator = models.BooleanField(default=True)
    balcony = models.DecimalField(decimal_places=2, max_digits=1000)
    floors = models.DecimalField(decimal_places=2, max_digits=100)
    noumber_of_house_in_each_floor = models.DecimalField(decimal_places=2, max_digits=100000000000)
    description = models.TextField(max_length=400)
    images = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    yard = models.DecimalField(decimal_places=2, max_digits=100000000000)
    area_of_ground = models.DecimalField(decimal_places=2, max_digits=100000000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_house = models.CharField(choices=TYPE_HOUSE, max_length=20)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    code_domain = models.IntegerField(default=0)




class Buy(models.Model):
    COUNTRY_CHOICES = [
        ('IR', 'Iran'),
    ]
    CITY_CHOICES = [
        ('TEH', 'Tehran'),
        ('MAS', 'Mashhad'),
        ('ESF', 'Esfehan'),
    ]
    ZONE_CHOICES = [
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),
        ('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
        ('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),
        ('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),
    ]
    TYPE_HOUSE = [
        ('APA', 'apartment'),
        ('VIL', 'villa'),
        ('LAN', 'land'),
    ]
    USE = [
        ('RES', 'residential'),
        ('COM', 'commercial'),
    ]
    country = models.CharField(choices=COUNTRY_CHOICES, default='IR', max_length=50)
    city = models.CharField(choices=CITY_CHOICES, default='TEH', max_length=50)
    zone = models.CharField(choices=ZONE_CHOICES, default='1', max_length=50)
    ghadr_o_sahm = models.DecimalField(decimal_places=2, max_digits=1000)
    price = models.DecimalField(decimal_places=2, max_digits=100000000000)
    area = models.DecimalField(decimal_places=2, max_digits=100000)
    number_of_rooms = models.DecimalField(max_digits=7,decimal_places=2)
    age_of_house = models.DecimalField(decimal_places=2, max_digits=100)
    parking = models.DecimalField(decimal_places=2, max_digits=100000000000)
    warehouse = models.DecimalField(decimal_places=2, max_digits=100000000000)
    elevator = models.BooleanField(default=True)
    balcony = models.DecimalField(decimal_places=2, max_digits=100000000000)
    floors = models.DecimalField(decimal_places=2, max_digits=100000000000)
    noumber_of_house_in_each_floor = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField(max_length=500)
    images = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    yard = models.DecimalField(decimal_places=2, max_digits=100000000000)
    area_of_ground = models.DecimalField(decimal_places=2, max_digits=100000000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_house = models.CharField(choices=TYPE_HOUSE, max_length=20)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    code_domain = models.IntegerField(default=0)
    for_exchange = models.BooleanField(default=False)

