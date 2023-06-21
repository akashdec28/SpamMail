from django.shortcuts import render,redirect
from siteadmin.models import*
from user.models import*
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    return render(request,"admin/index.html")


def login(request):
    return render(request,"admin/login.html")


def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    user=register_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        messages.add_message(request,messages.INFO,"Admin Logged In.")
        return render(request,"admin/loginhome.html")
    elif user.count()>0:
        request.session['id']=user[0].id
        messages.add_message(request,messages.INFO,"User Logged In.")
        return render(request,"admin/userhome.html")
    else:
        return redirect('login')

def hobiename(request):
    return render(request,"admin/hobiename.html")

def hobieAction(request):
    hobies=request.POST['hobies']
    user=hobiename_tb(name=hobies)
    user.save()
    messages.add_message(request,messages.INFO,"Added successfully")
    return redirect('hobiename')

def hobie(request):
    adminid=request.session['id']
    hobiename=hobiename_tb.objects.all()
    return render(request,"admin/hobie.html",{'data':hobiename})

def hobieAction(request):
    hobie=request.POST['hobie']
    discription=request.POST['discription']
    insert=hobie_tb(factorid=discription,hobieid_id=hobie)
    insert.save()
    messages.add_message(request,messages.INFO," Hobies Added Succesfully")
    return redirect('hobie')

def season(request):
    adminid=request.session['id']
    return render(request,"admin/season.html")

def seasonAction(request):
    seasonname=request.POST['seasonname']
    sinsert=season_tb(seasonname=seasonname)
    sinsert.save()
    messages.add_message(request,messages.INFO," Season Added Succesfully")
    return redirect('season')

def selectseason(request):
    adminid=request.session['id']
    seasonname=season_tb.objects.all()
    return render(request,"admin/selectseason.html",{'data':seasonname})

def seasonselectAction(request):
    season=request.POST['season']
    seasonfactor=request.POST['seasonfactor']
    sfnsert=seasonfactor_tb(seasonid_id=season,seasonfactor=seasonfactor)
    sfnsert.save()
    messages.add_message(request,messages.INFO," Seasons Enterd Succesfully")
    return redirect('selectseason')

def fourdrop(request):
    country=country_tb.objects.all()
    season=season_tb.objects.all()
    return render(request,"admin/fourdrop.html",{'country':country,'season':season})

def state(request):
    state=request.GET['country']
    state=state_tb.objects.filter(countryid_id=state)
    return render(request,"admin/userstate.html",{'state':state})

def factor(request):
    factor=request.GET['season']
    ufactor=seasonfactor_tb.objects.filter(seasonid_id=factor)
    return render(request,"admin/factor.html",{'factor':ufactor})

def fourdropAction(request):
    countryid=request.POST['country']
    stateid=request.POST['state']
    seasonid=request.POST['season']
    factorid=request.POST['factor']
    month=request.POST['month']
    fda=seasoncountry_tb(countryid_id=countryid,stateid_id=stateid,seasonid_id=seasonid,factorid_id=factorid,month=month)
    fda.save()
    messages.add_message(request,messages.INFO,"Successfull")
    return redirect('fourdrop')

def age(request):
    return render(request,"admin/age.html")

def ageAction(request):
    minage=request.POST['minage']
    maxage=request.POST['maxage']
    factor=request.POST['factor']
    a=agefactor_tb(minage=minage,maxage=maxage,factor=factor)
    a.save()
    messages.add_message(request,messages.INFO,"Added Successfully")
    return redirect('age')

def quickpasschange(request):
    adminid=request.session['id']
    apc=admin_tb.objects.filter(id=adminid)
    return render(request,"admin/adminquickpasschange.html")

def adminquickpasschangeAction(request):
    adminid=request.session['id']
    opass=request.POST['oldpass']
    npass=request.POST['newpass']
    cpass=request.POST['cnfpass']
    admin=admin_tb.objects.filter(id=adminid,password=opass)
    if admin.count()>0:
            if npass == cpass:
                change=admin_tb.objects.filter(id=adminid).update(password=npass)
                messages.add_message(request,messages.INFO,"Password Updated Successfully")
                return redirect('quickpasschange')
            else:
                messages.add_message(request,messages.INFO,"Password Not Equal")
                return redirect('quickpasschange')
    else:
        messages.add_message(request,messages.INFO," Current Password Does not Match")
        return redirect('quickpasschange')

def forgotpass(request):
    return render(request,"admin/forgotpass.html")

def forgotpassAction(request):
    username=request.POST['username']
    rtb=register_tb.objects.filter(username=username)
    if rtb.count()>0:
        request.session['id']=rtb[0].id
        return render(request,"admin/passchange.html",{'data':username})
    else:
        return redirect('forgotpass')

def checkpassAction(request):
    username=request.POST['username']
    name=request.POST['name']
    phone=request.POST['phone']
    rtb=register_tb.objects.filter(name=name,phone=phone)
    if rtb.count()>0:
        return render(request,"admin/changepassword.html",{'data':username})
    else:
        return redirect('checkpassAction')

def newpassAction(request):
    newpass=request.POST['newpass']
    cnfpass=request.POST['cnfpass']
    username=request.POST['username']
    if newpass == cnfpass:
        rtb=register_tb.objects.filter(username=username)
        if rtb.count()>0:
            request.session['id']=rtb[0].id
            userid=request.session['id']
            bpc=register_tb.objects.filter(id=userid).update(password=newpass)
            messages.add_message(request,messages.INFO,"User Password Updated Successfully")
            return redirect('index')
        else:
            return render(request,"admin/changepassword.html",{'data':username})

def usercheckforPC(request):
    getusername=request.GET['getusername']
    pc=register_tb.objects.filter(username=getusername)
    if pc.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})


