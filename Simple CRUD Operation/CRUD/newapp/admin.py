from django.contrib import admin
from .models import Member
# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_display="first_name","last_name","address"

admin.site.register(Member,ModelAdmin)