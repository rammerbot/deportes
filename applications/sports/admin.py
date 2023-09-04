from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Sports)
admin.site.register(SportCategories)
admin.site.register(Teams)
admin.site.register(Events)
admin.site.register(Result)