# Generated by Django 5.1.3 on 2024-11-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logo')),
                ('subtitle', models.TextField(max_length=500)),
                ('facbook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('instgram_link', models.URLField(blank=True, null=True)),
                ('phones', models.TextField(blank=True, max_length=500, null=True)),
                ('email', models.TextField(blank=True, max_length=500, null=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('call_us', models.CharField(blank=True, max_length=100, null=True)),
                ('email_us', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
