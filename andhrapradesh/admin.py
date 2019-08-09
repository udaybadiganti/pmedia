from django.contrib import admin
from .models import district, assemblies, public_complaints
# Register your models here.

admin.site.register(district)
admin.site.register(assemblies)
admin.site.register(public_complaints)
