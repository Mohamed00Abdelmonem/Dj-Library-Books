# Generated by Django 5.1.3 on 2025-01-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation_project', '0002_alter_graduationproject_doctor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduationprojectreaction',
            name='likes',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]