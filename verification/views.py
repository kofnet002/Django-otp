from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import User
import random
from .otp import MessageHandler

# Create your views here.
def homePage(request):
    if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
        return HttpResponse(" verified.")
    else:
        return HttpResponse(" Not verified.")


def registerPage(request):
    if request.method=="POST":
        # checking for existing user and then throw an error if there is one already
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")

        # creating new user and generate 6 long OTP code for the user
        otp=random.randrange(111111, 999999, 6)
        user=User.objects.create(
                username=request.POST.get('user_name'),
                phone_number=request.POST.get('phone_number'),
                otp=f'{otp}'
                )

        # otp via whatsapp
        if request.POST['methodOtp']=="methodOtpWhatsapp":
            messagehandler=MessageHandler(
                request.POST['phone_number'],
                otp).send_otp_via_whatsapp()

        # otp via SMS
        else:
            messagehandler=MessageHandler(
                request.POST['phone_number'],
                otp).send_otp_via_message()

        # redirecting user to OTP page to input the received OTP and setting a cookie with a lifetime of 10 minutes
        red=redirect(f'otp/{user.uid}/')
        red.set_cookie("can_otp_enter", True, max_age=600)
        return red  

    return render(request, 'verification/register.html')



def otpVerify(request, uid):
    if request.method == "POST":
        user=User.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter') != None: # checking if cookie exists
            if(user.otp == request.POST['otp']): # checking if user otp is equal to the generated otp
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"verification/otp.html", {'id':uid})
 
