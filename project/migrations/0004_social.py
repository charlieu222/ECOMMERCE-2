# Generated by Django 4.2 on 2023-04-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='social_images')),
            ],
        ),
    ]
