from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class hobiename_tb(models.Model):
    name=models.CharField(max_length=20)

class hobie_tb(models.Model):
    hobieid=models.ForeignKey(hobiename_tb,on_delete=models.CASCADE)
    factorid=models.CharField(max_length=20)

class season_tb(models.Model):
    seasonname=models.CharField(max_length=20)

class seasonfactor_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    seasonfactor=models.CharField(max_length=20)

class seasoncountry_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    countryid=models.ForeignKey('user.country_tb',on_delete=models.CASCADE)
    stateid=models.ForeignKey('user.state_tb',on_delete=models.CASCADE)
    factorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    month=models.IntegerField()

    