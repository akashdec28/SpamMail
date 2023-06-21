# Generated by Django 4.2 on 2023-05-31 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_seasonfactor_tb'),
        ('user', '0003_register_tb_sa'),
    ]

    operations = [
        migrations.CreateModel(
            name='userhobie_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobiename_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register_tb')),
            ],
        ),
    ]
