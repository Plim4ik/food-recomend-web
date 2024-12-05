from django.contrib import admin
from .models import Insurance, Request, User


# Register your models here.
@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'price')
    list_filter = ('created_at', 'updated_at')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'created_at', 'updated_at')
    search_fields = ('user', 'message')
    list_filter = ('created_at', 'updated_at')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'address', 'phone')
    search_fields = ('first_name', 'last_name', 'city', 'address', 'phone')
    list_filter = ('city', 'address', 'phone')