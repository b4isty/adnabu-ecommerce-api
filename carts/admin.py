from django.contrib import admin

from .models import Cart, Order

admin.site.register([Cart, Order])
