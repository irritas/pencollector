from django.contrib import admin
from .models import Ink, Pen, Refill

admin.site.register(Ink)
admin.site.register(Pen)
admin.site.register(Refill)