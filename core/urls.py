from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',about.home,name='home'),
    path('contact',about.contact,name='contact'),
    path('faq',about.faq,name='faq'),
    path('terms',about.terms, name='terms'),
    path('privpol',about.privpol, name='privpol'),
    path('user/signup',user.signup, name='signup'),
    path('user/login', user.user_login, name='login'),
    path('user/recover', user.recover, name='recover'),
    path('user/signup_confirm/<int:id>', user.signup_confirm, name='signup_confirm'),
    path('user/recover_confirm/<str:token>', user.recover_confirm, name='recover_confirm'),
    path('user/logout', user.user_logout, name='logout'),
    path('pricing', about.pricing, name='pricing'),
    path('comingsoon', about.comingsoon, name='comingsoon'),
    path('error/500', about.error_500, name='index'),
    path('error/404', about.error_404, name='index'),
    path('dashboard/profile', user.dash_profile, name='dash_profile'),
    path('dashboard/payment', user.dash_payment, name='dash_profile'),
    path('dashboard/notif', user.dash_notif, name='dash_profile'),
    path('creator', about.creator, name = 'creator'),
    path('develop', about.develop, name='develop'),
    path('view/<str:pagename>', page.view, name='develop'),
    path('edit_block/<int:block_id>', page.edit_block, name='devform'),
    path('creage/<int:block_id>', page.creative_agency, name='creative_agency'),
    path('multitask/<int:block_id>', page.multitasking, name='multitasking'),
    path('business/<int:block_id>', page.business, name='business'),
    path('shoping/<int:block_id>', page.shoping, name='shoping'),
    path('ordch/up/<int:block_id>', page.ordch_up, name='orderchange_up'),
    path('ordch/down/<int:block_id>', page.ordch_down, name='orderchange_down'),
    path('delete/<int:block_id>', page.delete, name='delete'),
]