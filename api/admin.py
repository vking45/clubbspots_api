from django.contrib import admin
from .models import Club
from .models import Media, Report

# Register your models here.
admin.site.register(Club)
admin.site.register(Media)
admin.site.register(Report)