from django.shortcuts import render,redirect
from django.core.mail import send_mail
from papernestapp.models import Product
from django.contrib import messages
from math import ceil
from django.conf import settings
from django.http import HttpResponse
from .models import Paper
# Create your views here.
def index(request):
    
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = [item['category'] for item in catprods]
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
        
    params={'allProds':allProds}
    
    return render(request, "index.html",params)

# def contact(request):
#     return render(request, "contact.html")

def about(request):
     return render(request, "about.html")

def contact(request):
    message_sent = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        reply_message = f"""
        Hello {name},

        Thanks for reaching out!

        We received your message:
        "{message}"

        We will get back to you as soon as possible.

        Best Regards,
        Paper Nest Team
        """

        send_mail(
            subject="Thanks for contacting Paper Nest!",
            message=reply_message,
            from_email='bashajuned143@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
        message_sent = True

    # 👇 Load products just like the home page
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = [item['category'] for item in catprods]
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    return render(request, "activate.html", {
        'message_sent': message_sent,
        'allProds': allProds
    })
def paper_list(request):
    category = request.GET.get('category')
    if category:
        papers = Paper.objects.filter(category=category)
    else:
        papers = Paper.objects.all()
    return render(request, 'papers.html', {'papers': papers})