# Generated by Django 4.2 on 2023-06-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_contact_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_tb',
            name='name',
            field=models.CharField(default='n', max_length=20),
        ),
    ]