from django.db import models

# Create your models here.
class country_tb(models.Model):
    country=models.CharField(max_length=25)
class state_tb(models.Model):
    state=models.CharField(max_length=25)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)

class register_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    country=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    sq=models.CharField(max_length=20)
    sa=models.CharField(max_length=20,default='abc')
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class userhobie_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobieid=models.ForeignKey('siteadmin.hobiename_tb',on_delete=models.CASCADE)

class agefactor_tb(models.Model):
    minage=models.IntegerField()
    maxage=models.IntegerField()
    factor=models.CharField(max_length=20)

class message_tb(models.Model):
    sendersid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='sender')
    reciversid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='reciver')
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    filterstatus=models.CharField(max_length=20)

class trash_tb(models.Model):
    messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    reciverid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

class contact_tb(models.Model):
    contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='contact')
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='user')
    name=models.CharField(max_length=20,default='n')
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)

class blacklist_tb(models.Model):
    contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='contact1')
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='user2')
    name=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)

class customerhobiefactor_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobieid=models.ForeignKey('siteadmin.hobiename_tb',on_delete=models.CASCADE)
    factorid=models.ForeignKey('siteadmin.hobie_tb',on_delete=models.CASCADE)

class costomeragefactor_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey(agefactor_tb,on_delete=models.CASCADE)

class customerseasoncountry_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey('siteadmin.seasonfactor_tb',on_delete=models.CASCADE)








