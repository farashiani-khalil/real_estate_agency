# Generated by Django 3.1.6 on 2021-04-01 13:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('IR', 'Iran')], default='IR', max_length=50)),
                ('city', models.CharField(choices=[('TEH', 'Tehran'), ('MAS', 'Mashhad'), ('ESF', 'Esfehan')], default='TEH', max_length=50)),
                ('zone', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], default='1', max_length=50)),
                ('ghadr_o_sahm', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('area', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('number_of_rooms', models.DecimalField(decimal_places=2, max_digits=7)),
                ('age_of_house', models.DecimalField(decimal_places=2, max_digits=100)),
                ('parking', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('warehouse', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('elevator', models.BooleanField(default=True)),
                ('balcony', models.DecimalField(decimal_places=2, max_digits=100000000)),
                ('floors', models.DecimalField(decimal_places=2, max_digits=10000000)),
                ('noumber_of_house_in_each_floor', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.TextField(max_length=500)),
                ('yard', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('area_of_ground', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('type_house', models.CharField(choices=[('APA', 'apartment'), ('VIL', 'villa'), ('LAN', 'land')], max_length=20)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
                ('code_domain', models.IntegerField(default=0)),
                ('for_exchange', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('IR', 'Iran')], default='IR', max_length=50)),
                ('city', models.CharField(choices=[('TEH', 'Tehran'), ('MAS', 'Mashhad'), ('ESF', 'Esfehan')], default='TEH', max_length=50)),
                ('zone', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], default='1', max_length=50)),
                ('mortgage', models.DecimalField(decimal_places=2, default=0, max_digits=100000000000)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('area', models.DecimalField(decimal_places=2, max_digits=1000000)),
                ('number_of_rooms', models.DecimalField(decimal_places=2, max_digits=7)),
                ('age_of_house', models.DecimalField(decimal_places=2, max_digits=100)),
                ('parking', models.DecimalField(decimal_places=2, max_digits=100)),
                ('warehouse', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('elevator', models.BooleanField(default=True)),
                ('balcony', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('floors', models.DecimalField(decimal_places=2, max_digits=100)),
                ('noumber_of_house_in_each_floor', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('description', models.TextField(max_length=400)),
                ('yard', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('area_of_ground', models.DecimalField(decimal_places=2, max_digits=100000000000)),
                ('type_house', models.CharField(choices=[('APA', 'apartment'), ('VIL', 'villa'), ('LAN', 'land')], max_length=20)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
                ('code_domain', models.IntegerField(default=0)),
                ('images', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Domain.image')),
            ],
        ),
    ]
