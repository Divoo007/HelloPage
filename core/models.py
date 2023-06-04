from django.db import models
from django.contrib.auth.forms import User
from core.utils import crypto_utils
import json
# Create your models here.


class SignUp(models.Model):
    name = models.CharField(max_length=128)
    pagename = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=32, default=crypto_utils.token_alphanum16)
    otp = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class HPUser(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pagename = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Recover(models.Model):
    hp_user = models.ForeignKey(HPUser, on_delete=models.PROTECT)
    token = models.CharField(max_length=32, default=crypto_utils.token_alphanum16)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.IntegerField()
    subject = models.CharField(max_length=512)
    text = models.CharField(max_length=4096)

creativeagency = {
    'title': 'random',
    'subtitle': 'random',
    'videolink': 'https://www.youtube.com/watch?v=8HmtP1dGk-A&t=4s',
    'videotitle': 'random'
}

class BlockTemplate(models.Model):
    html = models.TextField()
    data = models.TextField()

class Block(models.Model):
    temp = models.ForeignKey(BlockTemplate, on_delete=models.PROTECT)
    data = models.TextField()
    hp_user = models.ForeignKey(HPUser, on_delete=models.PROTECT)
    order = models.IntegerField(default=0)







