# Generated by Django 5.1.3 on 2024-12-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='national_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]