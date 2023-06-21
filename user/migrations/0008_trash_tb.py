# Generated by Django 4.2 on 2023-06-02 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_uadmin_tb_message_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='trash_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('messageid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.message_tb')),
                ('reciverid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]