from django.contrib import admin
from .models import News, Home, Team, Video, Publicity
# Register your models here.

admin.site.register(Home)
admin.site.register(News)
admin.site.register(Team)
admin.site.register(Video)
admin.site.register(Publicity)