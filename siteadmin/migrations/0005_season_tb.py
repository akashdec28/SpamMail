# Generated by Django 4.2 on 2023-05-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_rename_hobie_td_hobie_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='season_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasonname', models.CharField(max_length=20)),
            ],
        ),
    ]
