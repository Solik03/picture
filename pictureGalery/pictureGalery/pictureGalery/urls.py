"""
Definition of urls for pictureGalery.
"""
"""
Definition of urls for picture.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
	url(r'^stile1$',app.views.stile , name='stile'),
	url(r'^register$',app.views.registration , name='reg'),
	url(r'^register/process$',app.views.register_ajax, name='auth'),
	url(r'^login/process$',app.views.login, name='login'),
	url(r'^paintings$',app.views.paintings, name='paint'),
    url(r'^$', app.views.home, name='home'),
	url(r'^logout', app.views.logout_user, name='logout'),
	url(r'^cart/ajax$', app.views.cart_ajax, name='cart'),
	url(r'^cart$', app.views.cart, name='cart'),
	url(r'^cart/del$', app.views.cart_del, name='cart_del'),
	url(r'^cart/save$', app.views.save_cart, name='save'),
	url(r'^message$', app.views.message, name='message'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]