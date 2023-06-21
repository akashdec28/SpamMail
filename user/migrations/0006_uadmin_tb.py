# Generated by Django 4.2 on 2023-06-01 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_agefactor_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='uadmin_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('filterstatus', models.CharField(max_length=20)),
                ('reciversid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciver', to='user.register_tb')),
                ('sendersid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='user.register_tb')),
            ],
        ),
    ]
