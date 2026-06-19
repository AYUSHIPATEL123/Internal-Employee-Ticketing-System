from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=('id','summary','employee','assignee','status','priority','created_at')
    list_filter=('status','priority')
    list_display_links=('summary',)