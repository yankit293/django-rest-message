from django.contrib import admin
from .models import messages

# Register your models here.
@admin.register(messages)
class messageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_at', 'updated_at', 'created_by'] 
