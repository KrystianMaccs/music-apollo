# Generated by Django 3.2.7 on 2022-04-14 14:20

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+41524204242', max_length=30, region=None, verbose_name='Phone Number')),
                ('about_me', models.TextField(default='say something about yourself', verbose_name='About me')),
                ('profile_photo', models.ImageField(default='/profile_default.png', upload_to='', verbose_name='Profile Photo')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=20, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(default='KE', max_length=2, verbose_name='Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
