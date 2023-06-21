from django.shortcuts import render,redirect
from django.contrib import messages
from siteadmin.models import*
from user.models import*
import datetime
from django.http import JsonResponse



# Create your views here.

def userregistration(request):
    country=country_tb.objects.all()
    hobies=hobiename_tb.objects.all()
    return render(request,"user/userregistration.html",{'country':country,'hobies':hobies})

def state(request):
    state=request.GET['country']
    vs=state_tb.objects.filter(countryid_id=state)
    return render(request,"user/state.html",{'state':vs})

def userregisterAction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    dob=request.POST['dob']
    sq=request.POST['sq']
    sa=request.POST['sa']
    country=request.POST['country']
    state=request.POST['state']
    username=request.POST['username']
    password=request.POST['password']
    hobies=request.POST.getlist('hobies')
    user=register_tb(name=name,address=address,gender=gender,phone=phone,dob=dob,sq=sq,sa=sa,country_id=country,state_id=state,username=username+'@gmail.com',password=password)
    user.save()
    for hid in hobies:
        shobies=userhobie_tb(hobieid_id=hid,userid_id=user.id)
        shobies.save()
    messages.add_message(request,messages.INFO,"Registration Successfull")
    return redirect('userregistration')

def sendmessage(request):
    return render(request,"user/sendmessage.html")

def sendmessageAction(request):
    sender=request.session['id']
    reciversid=request.POST['reciversid']
    rec=register_tb.objects.get(username=reciversid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    msg=message_tb(sendersid_id=sender,reciversid=rec,subject=subject,message=message,date=date,time=time,status='pending',filterstatus='pending')
    msg.save()
    messages.add_message(request,messages.INFO,"Sent")
    return redirect('sendmessage')

def checkreciversid(request):
    reciversid=request.GET['recivername']
    cr=register_tb.objects.filter(username=reciversid)
    if cr.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})

def viewmessage(request):
    userid=request.session['id']
    status=['pending','deleted by reciver']
    vm=message_tb.objects.filter(status__in=status,sendersid_id=userid)
    return render(request,"user/viewmessage.html",{'viewmessage':vm})

def deletemsg(request,id):
    m=message_tb.objects.filter(id=id)
    status=m[0].status
    if status == 'deleted by reciver':
        d=message_tb.objects.filter(id=id).delete()
        return redirect('viewmessage')
    if status == 'pending':
        u=message_tb.objects.filter(id=id).update(status="deleted by sender")
    return redirect('viewmessage')

def viewrecivedmsg(request):
    userid=request.session['id']
    status=['pending','deleted by sender']
    #vrm=message_tb.objects.filter(reciversid_id=userid,status__in=status).exclude(id__in=trash_tb.objects.filter(reciversid_id=userid).values('messageid_id'))
    age=costomeragefactor_tb.objects.filter(userid_id=userid)
    for a in age :
        msg=message_tb.objects.filter(reciversid_id=userid,filterstatus="pending",message__icontains=a.factorid.factor).exclude(sendersid__in=blacklist_tb.objects.filter(userid_id=userid).values('contactid')).update(filterstatus="filterd")
    hobies=customerhobiefactor_tb.objects.filter(userid_id=userid)
    for h in hobies :
        msg=message_tb.objects.filter(reciversid_id=userid,filterstatus="pending",message__icontains=h.factorid.factorid).exclude(sendersid__in=blacklist_tb.objects.filter(userid_id=userid).values('contactid')).update(filterstatus="filterd")
    season=customerseasoncountry_tb.objects.filter(userid_id=userid)
    for s in season :
        msg=message_tb.objects.filter(reciversid_id=userid,filterstatus="pending",message__icontains=s.factorid.seasonfactor).exclude(sendersid__in=blacklist_tb.objects.filter(userid_id=userid).values('contactid')).update(filterstatus="filterd")
    contact=contact_tb.objects.filter(userid_id=userid)
    for c in contact :
        cn=message_tb.objects.filter(reciversid_id=userid,filterstatus="pending",sendersid_id=c.contactid).update(filterstatus="filterd")
    inbox=message_tb.objects.filter(reciversid_id=userid,status__in=status,filterstatus="filterd").exclude(id__in=trash_tb.objects.filter(reciverid_id=userid).values('messageid_id'))
    return render(request,"user/viewrecivedmsg.html",{'recivedmsg':inbox})

def trashAction(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    c=request.POST.getlist('trash')
    for t in c:
        z=message_tb.objects.get(id=t)
        reciverid=request.session['id']
        t=trash_tb(messageid=z,reciverid_id=reciverid,date=date,time=time)
        t.save()
    return redirect('viewrecivedmsg')

def viewtrash(request):
    userid=request.session['id']
    vt=trash_tb.objects.filter(reciverid_id=userid)
    return render(request,"user/viewtrash.html",{'viewtrash':vt})

def deletetrash(request,id):
    dt=trash_tb.objects.filter(id=id)
    m=message_tb.objects.filter(id=dt[0].messageid_id)
    status=m[0].status
    if status == "pending":
        message_tb.objects.filter(id=dt[0].messageid_id).update(status="deleted by reciver ")
        ttd=trash_tb.objects.filter(id=id).delete()
    return redirect('viewtrash')

def forward(request,id):
    f=message_tb.objects.filter(id=id)
    return render(request,"user/forward.html",{'viewfwdmsg':f})

def fwdcheckreciversid(request):
    reciversid=request.GET['recivername']
    fmcrn=register_tb.objects.filter(username=reciversid)
    if fmcrn.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})

def forwardAction(request):
    userid=request.session['id']
    reciversid=request.POST['reciversid']
    frec=register_tb.objects.get(username=reciversid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    sfm=message_tb(sendersid_id=userid,reciversid=frec,subject=subject,message=message,date=date,time=time,status='pending',filterstatus='pending')
    sfm.save()
    messages.add_message(request,messages.INFO,"Message Forwarded")
    return redirect('viewrecivedmsg')

def reply(request,id):
    r=message_tb.objects.filter(id=id)
    return render(request,"user/reply.html",{'reply':r})

def replyAction(request):
    userid=request.session['id']
    reciversid=request.POST['reciversid']
    rrec=register_tb.objects.get(username=reciversid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    sfm=message_tb(sendersid_id=userid,reciversid=rrec,subject=subject,message=message,date=date,time=time,status='pending',filterstatus='pending')
    sfm.save()
    messages.add_message(request,messages.INFO,"Your Reply has been Sent")
    return redirect('viewrecivedmsg')

def newcontact(request):
    return render(request,"user/newcontact.html")

def validatereciver(request):
    reciversid=request.GET['recivername']
    crm=register_tb.objects.filter(username=reciversid)
    if crm.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})

def newcontactAction(request):
    userid=request.session['id']
    contactid=request.POST['contactid']
    ca=register_tb.objects.get(username=contactid)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    c=contact_tb(userid_id=userid,contactid=ca,name=name,remarks=remarks,date=date,time=time,)
    c.save()
    messages.add_message(request,messages.INFO,"Contact Added")
    return redirect('newcontact')

def viewcontacts(request):
    userid=request.session['id']
    vc=contact_tb.objects.filter(userid_id=userid)
    return render(request,"user/viewcontacts.html",{'contacts':vc})

def deletecontact(request,id):
    dc=contact_tb.objects.filter(id=id).delete()
    return redirect('viewcontacts')

def blacklist(request):
    return render(request,"user/blacklist.html")

def blacklistvalidation(request):
    reciversid=request.GET['recivername']
    crm=register_tb.objects.filter(username=reciversid)
    if crm.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})

def blacklistAction(request):
    userid=request.session['id']
    contactid=request.POST['contactid']
    ca=register_tb.objects.get(username=contactid)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    c=blacklist_tb(userid_id=userid,contactid=ca,name=name,remarks=remarks,date=date,time=time,)
    c.save()
    messages.add_message(request,messages.INFO,"Contact Blocked")
    return redirect('blacklist')

def viewblacklist(request):
    userid=request.session['id']
    vb=blacklist_tb.objects.all()
    return render(request,"user/viewblacklist.html",{'blacklist':vb})

def deleteblacklist(request,id):
    db=blacklist_tb.objects.filter(id=id).delete()
    return redirect('user/viewblacklist')


def movetoblacklist(request,id):
    userid=request.session['id']
    contact=contact_tb.objects.filter(id=id)
    name=contact[0].name
    remarks=contact[0].remarks
    contactid=contact[0].contactid
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    blacklist=blacklist_tb(userid_id=userid,contactid=contactid,name=name,remarks=remarks,date=date,time=time)
    blacklist.save()
    contact.delete()
    return redirect('viewcontacts')

def uhobie(request):
    userid=request.session['id']
    uhv=userhobie_tb.objects.filter(userid_id=userid)
    return render(request,"user/uhobie.html",{'hobies':uhv})

def chobie(request):
    factor=request.GET['hname']
    df=hobie_tb.objects.filter(hobieid_id=factor)
    return render(request,"user/dropfactor.html",{'factors':df})

def uhobieAction(request):
    userid=request.session['id']
    hobieid=request.POST['hobie']
    factorid=request.POST['factor']
    suh=customerhobiefactor_tb(userid_id=userid,hobieid_id=hobieid,factorid_id=factorid)
    suh.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('uhobie')

def yourage(request):
    userid=request.session['id']
    c=register_tb.objects.filter(id=userid)
    birthyear=c[0].dob
    spl=birthyear.split('-')
    p=spl[0]
    date=datetime.date.today()
    currentyear=date.year
    age=currentyear - int(p)
    factor=agefactor_tb.objects.filter(minage__lte=age,maxage__gte=age)
    return render(request,"user/yourage.html",{'age':factor})

def yourageAction(request):
    userid=request.session['id']
    factorid=request.POST['factor']
    caf=costomeragefactor_tb(userid_id=userid,factorid_id=factorid)
    caf.save()
    messages.add_message(request,messages.INFO,"Age Category Added")
    return redirect('yourage')

def userseason(request):
    userid=request.session['id']
    checkuser=register_tb.objects.filter(id=userid)
    country=checkuser[0].country_id
    state=checkuser[0].state_id
    date=datetime.date.today()
    month=date.month
    o=seasoncountry_tb.objects.filter(countryid_id=country,stateid_id=state,month=month)
    return render(request,"user/season.html",{'season':o})

def userseasonAction(request):
    userid=request.session['id']
    factorid=request.POST['factor']
    csc=customerseasoncountry_tb(userid_id=userid,factorid_id=factorid)
    csc.save()
    messages.add_message(request,messages.INFO,"Season Factor Added")
    return redirect('season')

def viewspam(request):
    userid=request.session['id']
    status=['pending','deleted by sender']
    m=message_tb.objects.filter(filterstatus='pending',status__in=status,reciversid_id=userid)
    return render(request,"user/viewspam.html",{'spam':m})

def deletespammsg(request,id):
    userid=request.session['id']
    mx=message_tb.objects.filter(id=id)
    status=mx[0].status
    if status == 'deleted by sender':
        smd=message_tb.objects.filter(id=id).delete()
    else:
        message_tb.objects.filter(id=id).update(status='deleted by reciver')
    return redirect('viewspam')

def logout(request):
    logout=request.session.flush()
    return redirect('login')

def userprofileupdate(request):
    userid=request.session['id']
    pu=register_tb.objects.filter(id=userid)
    country=country_tb.objects.all()
    hobies=hobiename_tb.objects.all()
    uhobies=userhobie_tb.objects.filter(userid_id=userid)
    return render(request,"user/userprofileupdate.html",{'update':pu,'country':country,'hobies':hobies,'uhobies':uhobies})

def userstateupdate(request):
    state=request.GET['country']
    vs=state_tb.objects.filter(countryid_id=state)
    return render(request,"user/userstateupdate.html",{'state':vs})


def userprofileupdateAction(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    dob=request.POST['dob']
    sq=request.POST['sq']
    sa=request.POST['sa']
    country=request.POST['country']
    state=request.POST['state']
    username=request.POST['username']
    password=request.POST['password']
    hobies=request.POST.getlist('hobies')
    delhobie=userhobie_tb.objects.filter(userid_id=id).delete()
    user=register_tb.objects.filter(id=id).update(name=name,address=address,gender=gender,phone=phone,dob=dob,sq=sq,sa=sa,country_id=country,state_id=state,username=username+'@gmail.com',password=password)
    for hid in hobies:
        shobies=userhobie_tb(hobieid_id=hid,userid_id=id)
        shobies.save()
    messages.add_message(request,messages.INFO,"Profile Updated Successfully")
    return redirect('userprofileupdate')

def userquickpasschange(request):
    userid=request.session['id']
    apc=register_tb.objects.filter(id=userid)
    return render(request,"user/userquickpasschange.html")

def userquickpasschangeAction(request):
    userid=request.session['id']
    opass=request.POST['oldpass']
    npass=request.POST['newpass']
    cpass=request.POST['cnfpass']
    admin=register_tb.objects.filter(id=userid,password=opass)
    if admin.count()>0:
            if npass == cpass:
                change=register_tb.objects.filter(id=userid).update(password=npass)
                messages.add_message(request,messages.INFO,"Password Updated Successfully")
                return redirect('userquickpasschange')
            else: 
                messages.add_message(request,messages.INFO,"Password Not Equal")
                return redirect('userquickpasschange')
    else:
        messages.add_message(request,messages.INFO," Current Password Does not Match")
        return redirect('userquickpasschange')








    

























