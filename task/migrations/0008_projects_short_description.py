# Generated by Django 3.2.6 on 2021-10-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_profile_image_i'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
