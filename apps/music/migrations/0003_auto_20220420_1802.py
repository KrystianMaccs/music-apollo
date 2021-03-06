# Generated by Django 3.2.7 on 2022-04-20 17:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20220414_1520'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='collection',
            managers=[
                ('genres', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='song',
            managers=[
                ('tracks', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='artiste',
            field=models.CharField(default='Juice WRLD', max_length=50),
        ),
    ]
