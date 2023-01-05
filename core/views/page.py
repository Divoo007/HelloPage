import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.mail import EmailMessage
import hp.settings as site_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from core.models import Contact, HPUser, Block, BlockTemplate
from core.form import ContactForm, DevForm
from django.contrib.auth.models import User
from django.template import Template, Context


def view(request,pagename):
    hpdev = False
    hp_user = HPUser.objects.get(pagename=pagename)
    blocks = Block.objects.filter(hp_user=hp_user).order_by('order')
    block_htmls=[]
    for block in blocks:
        html_temp = Template(block.temp.html)
        data = json.loads(block.data)
        context = Context(data)
        block_htmls.append({'id':block.id,'html':html_temp.render(context), 'hp_user':hp_user})

    if hp_user.user == request.user:
        hpdev = True
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta, 'blocks': block_htmls, 'hpdev': hpdev}
    return render(request, 'core/page/demo-creative-agency.html', context)

def edit_block(request,block_id):
    if request.user.is_authenticated:
        hp_user = HPUser.objects.get(user=request.user)
    else:
        return redirect('/user/login')
    block = Block.objects.get(id=block_id)
    if block.hp_user != hp_user:
        return redirect('/user/login')
    data = json.loads(block.data)
    if request.method == 'POST':
        for key in data:
            data[key] = request.POST[key]
        block.data = json.dumps(data)
        block.save()
        return redirect('/view/'+ str(hp_user.pagename))
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta, 'data':data}
    return render(request, 'core/devform.html', context)

def ordch_up(request, block_id):
    block = Block.objects.get(id=block_id)
    hp_user = HPUser.objects.get(user=request.user)
    next_block = Block.objects.filter(hp_user=hp_user, order=block.order-1)[0]
    next_block.order = next_block.order+1
    block.order = block.order-1
    next_block.save()
    block.save()
    return redirect('/view/'+ str(hp_user.pagename))

def ordch_down(request, block_id):
    block = Block.objects.get(id=block_id)
    hp_user = HPUser.objects.get(user=request.user)
    next_block = Block.objects.filter(hp_user=hp_user, order=block.order+1)[0]
    next_block.order = next_block.order-1
    block.order = block.order+1
    next_block.save()
    block.save()
    return redirect('/view/'+ str(hp_user.pagename))

def delete(request, block_id):
    block = Block.objects.get(id=block_id)
    block = block.delete()
    hp_user = HPUser.objects.get(user=request.user)
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta}
    return redirect('/view/'+ str(hp_user.pagename))

def creative_agency(request, block_id):
    template_id = BlockTemplate.objects.get(id=1)
    hp_user = HPUser.objects.get(user=request.user)
    num_blocks = Block.objects.filter(hp_user=hp_user).count()
    bl_order = num_blocks+1
    block = Block.objects.create(temp=template_id,data='{"title": "Creativity beyond imagination", "subtitle": "We will help to bring your wildest ideas to life.", "videotitle": "Watch who, how and where"}', hp_user=hp_user, order=int(bl_order))
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta}
    return redirect('/view/'+ str(hp_user.pagename))

def multitasking(request, block_id):
    template_id = BlockTemplate.objects.get(id=2)
    hp_user = HPUser.objects.get(user=request.user)
    num_blocks = Block.objects.filter(hp_user=hp_user).count()
    bl_order = num_blocks+1
    block = Block.objects.create(temp=template_id,data='{"title": "Creativity beyond imagination", "subtitle": "We will help to bring your wildest ideas to life.", "videotitle": "Watch who, how and where"}', hp_user=hp_user, order=int(bl_order))
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta}
    return redirect('/view/'+ str(hp_user.pagename))

def business(request, block_id):
    template_id = BlockTemplate.objects.get(id=3)
    hp_user = HPUser.objects.get(user=request.user)
    num_blocks = Block.objects.filter(hp_user=hp_user).count()
    bl_order = num_blocks+1
    block = Block.objects.create(temp=template_id,data='{"title":"Fast way to achieve your goals in business", "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud.","video_url":"https://www.youtube.com/watch?v=8HmtP1dGk-A","video_text":"Get to know us better","CTA_heading":"Get a free consultation","phone_number":"+ 1 526 220 0459","image":"hero-img.jpg"}', hp_user=hp_user, order=int(bl_order))
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta}
    return redirect('/view/'+ str(hp_user.pagename))

def shoping(request, block_id):
    template_id = BlockTemplate.objects.get(id=4)
    hp_user = HPUser.objects.get(user=request.user)
    num_blocks = Block.objects.filter(hp_user=hp_user).count()
    bl_order = num_blocks+1
    block = Block.objects.create(temp=template_id,data='{"item_1":"Outdoor HD Cloud Security Camera","item_1_subtitle":"Stay connected 24/7. Free trial for 30 days","item_1_price":"$45.00","item_2":"Running Sneaker Sports Collection","item_2_subtitle":"Run like never before. Money back gaurantee","item_2_price":"$99.00","item_3":"Wireless Virtual Reality Headset","item_3_subtitle":"Run like never before. Money back guarantee","item_3_price":"$180.00"}', hp_user=hp_user, order=int(bl_order))
    meta = {
        'title': 'Frequently Asked Questions | HelloPage'
    }
    context = {'meta': meta}
    return redirect('/view/'+ str(hp_user.pagename))






