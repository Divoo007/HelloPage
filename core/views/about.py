from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.mail import EmailMessage
import hp.settings as site_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from core.models import Contact, HPUser
from core.form import ContactForm
from django.contrib.auth.models import User





def home(request):
    submitted = False
    meta = {'title': 'Home | HelloPage'}
    usr =None
    if request.user.is_authenticated:
        usr=HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr':usr}
    return render(request, 'core/home.html', context)

def contact(request):
    submitted = False
    usr =None
    if request.method == 'POST':
        cont_form = ContactForm(request.POST)
        if cont_form.is_valid():
            cont = cont_form.save()
            html_content = 'Name: %s<br/>Email: %s<br/>Subject: %s<br/>Phone: %s<br/>Text: %s<br/>' % (cont.name, cont.email, cont.subject, cont.phone, cont.text)
            msg = EmailMessage(subject='Contact on HelloPage',
                               body=html_content,
                               from_email=site_settings.DEFAULT_FROM_EMAIL,
                               to=[site_settings.SUPPORT_EMAIL],
                               bcc=[site_settings.ADMIN_EMAIL], )
            msg.content_subtype = "html"
            msg.send(fail_silently=False)
            submitted = True
    meta = {
        'title': 'Contact Us | HelloPage'
    }
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/contact.html', context)

def faq(request):
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/faq.html', context)

def privpol(request):
    meta = {
        'title': 'Privacy & Policy | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/comingsoon.html', context)

def terms(request):
    meta = {
        'title': 'Terms & Conditions | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/comingsoon.html', context)

def pricing(request):
    meta = {
        'title': 'Pricing | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/pricing.html', context)

def comingsoon(request):
    meta = {
        'title': 'Coming Soon | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/comingsoon.html', context)

def error_404(request):
    meta = {
        'title': 'Error 404 | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/404.html', context)

def error_500(request):
    meta = {
        'title': 'Error 500 | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/500.html', context)

def base(request):
    meta = {
        'title': 'Comments | HelloPage'
    }
    usr =None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/base.html', context)

def creator(request):
    meta = {
        'title': 'The Creator | HelloPage'
    }
    usr = None
    if request.user.is_authenticated:
        usr = HPUser.objects.get(user=request.user)
    context = {'meta': meta, 'usr': usr}
    return render(request, 'core/comingsoon.html', context)

def develop(request):
    comesoon = False
    meta = {
        'title': 'Start Developing | HelloPage'
    }
    usr = None
    if request.user.is_authenticated:
        usr = HPUser.objects.filter(user=request.user)
    if request.method == 'POST':
        comesoon = True

    context = {'meta': meta, 'usr': usr, 'comesoon':comesoon}
    return render(request, 'core/develop.html', context)












