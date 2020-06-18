from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Auser)
admin.site.register(Patient)
admin.site.register(Herb)
admin.site.register(Record)
admin.site.register(Prescription)

