"""
URL configuration for spammail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from user import views as userview
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('hobiename/',adminview.hobiename,name="hobiename"),
    path('hobieAction/',adminview.hobieAction,name="hobieAction"),
    path('hobie/',adminview.hobie,name="hobie"),
    path('hobieAction/',adminview.hobieAction,name="hobieAction"),
    path('season/',adminview.season,name="season"),
    path('seasonselectAction/',adminview.seasonselectAction,name="seasonselectAction"),
    path('seasonAction/',adminview.seasonAction,name="seasonAction"),
    path('selectseason/',adminview.selectseason,name="selectseason"),
    path('userregistration/',userview.userregistration,name="userregistration"),
    path('userregisterAction/',userview.userregisterAction,name="userregisterAction"),
    path('state/',userview.state,name="state"),
    path('fourdrop/',adminview.fourdrop,name="fourdrop"),
    path('state/',adminview.state,name="state"),
    path('factor/',adminview.factor,name="factor"),
    path('fourdropAction/',adminview.fourdropAction,name="fourdropAction"),
    path('age/',adminview.age,name="age"),
    path('ageAction/',adminview.ageAction,name="ageAction"),
    path('sendmessage/',userview.sendmessage,name="sendmessage"),
    path('sendmessageAction/',userview.sendmessageAction,name="sendmessageAction"),
    path('checkreciversid/',userview.checkreciversid,name="checkreciversid"),
    path('viewmessage/',userview.viewmessage,name="viewmessage"),
    path('deletemsg<int:id>/',userview.deletemsg,name="deletemsg"),
    path('viewrecivedmsg/',userview.viewrecivedmsg,name="viewrecivedmsg"),
    path('trashAction/',userview.trashAction,name="trashAction"),
    path('viewtrash/',userview.viewtrash,name="viewtrash"),
    path('deletetrash<int:id>/',userview.deletetrash,name="deletetrash"),
    path('forward<int:id>/',userview.forward,name="forward"),
    path('fwdcheckreciversid/',userview.fwdcheckreciversid,name="fwdcheckreciversid"),
    path('forwardAction/',userview.forwardAction,name="forwardAction"),
    path('reply<int:id>/',userview.reply,name="reply"),
    path('replyAction/',userview.replyAction,name="replyAction"),
    path('newcontact/',userview.newcontact,name="newcontact"),
    path('newcontactAction/',userview.newcontactAction,name="newcontactAction"),
    path('validatereciver/',userview.validatereciver,name="validatereciver"),
    path('viewcontacts/',userview.viewcontacts,name="viewcontacts"),
    path('deletecontact<int:id>/',userview.deletecontact,name="deletecontact"),
    path('blacklist/',userview.blacklist,name="blacklist"),
    path('blacklistvalidation/',userview.blacklistvalidation,name="blacklistvalidation"),
    path('blacklistAction/',userview.blacklistAction,name="blacklistAction"),
    path('viewblacklist/',userview.viewblacklist,name="viewblacklist"),
    path('deleteblacklist<int:id>/',userview.deleteblacklist,name="deleteblacklist"),
    path('movetoblacklist<int:id>/',userview.movetoblacklist,name="movetoblacklist"),
    path('uhobie/',userview.uhobie,name="uhobie"),
    path('uhobieAction/',userview.uhobieAction,name="uhobieAction"),
    path('chobie/',userview.chobie,name="chobie"),
    path('yourage/',userview.yourage,name="yourage"),
    path('yourageAction/',userview.yourageAction,name="yourageAction"),
    path('userseason/',userview.userseason,name="userseason"),
    path('userseasonAction/',userview.userseasonAction,name="userseasonAction"),
    path('viewspam/',userview.viewspam,name="viewspam"),
    path('deletespammsg<int:id>/',userview.deletespammsg,name="deletespammsg"),
    path('logout/',userview.logout,name="logout"),
    path('userprofileupdate/',userview.userprofileupdate,name="userprofileupdate"),
    path('userprofileupdateAction/',userview.userprofileupdateAction,name="userprofileupdateAction"),
    path('userstateupdate/',userview.userstateupdate,name="userstateupdate"),
    path('quickpasschange/',adminview.quickpasschange,name="quickpasschange"),
    path('adminquickpasschangeAction/',adminview.adminquickpasschangeAction,name="adminquickpasschangeAction"),
    path('userquickpasschange/',userview.userquickpasschange,name="userquickpasschange"),
    path('userquickpasschangeAction/',userview.userquickpasschangeAction,name="userquickpasschangeAction"),
    path('forgotpass/',adminview.forgotpass,name="forgotpass"),
    path('forgotpassAction/',adminview.forgotpassAction,name="forgotpassAction"),
    path('checkpassAction/',adminview.checkpassAction,name="checkpassAction"),
    path('newpassAction/',adminview.newpassAction,name="newpassAction"),
    path('usercheckforPC/',adminview.usercheckforPC,name="usercheckforPC")
    


]
