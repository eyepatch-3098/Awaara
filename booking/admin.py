from django.contrib import admin
from .models import BookingDetail, Payment
# Register your models here.

admin.site.register(BookingDetail)
admin.site.register(Payment)