# Generated by Django 3.1.4 on 2020-12-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201219_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photo_class2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
