from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import TokenGenerator,account_activation_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def signup(request):
    if request.method == 'POST':
        email=request.POST["email"]
        password=request.POST["pass1"]
        comfirm_password=request.POST["pass2"]
        if password!=comfirm_password:
            messages.warning(request,"password is not matching!") 
            return render(request,"juned/signup.html")
        
        try:
            if User.objects.get(username=email):
                 messages.info(request,"Email is taken")
                # return HttpResponse("email already exist")
                 return render(request,"juned/signup.html")
        except Exception as identifier:
            pass
        
        user=User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject="Active Your Account"
        message=render_to_string("activate.html",{
            'user':user,
            'domain':'127.0.0.1:8000',#it is very iportant
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
        
        email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,
        [email])
        email_message.send()
        messages.success(request,"Hey Buddy Activate Your Account by Clicking the link")
        return redirect('/auth/login/')
        # return HttpResponse(f"User created:{email}")#doubt
    return render(request,"juned/signup.html")

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login/')#doubt
        return render(request,'activatefail.html')
    
    

def handlelogin(request):
    return render(request,"juned/login.html")

def handlelogout(request):
    return redirect('/auth/login')