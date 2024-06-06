from django.contrib import admin
from main.models import Original, Translate, Summary

admin.site.register(Original)
admin.site.register(Translate)
admin.site.register(Summary)
# Register your models here.