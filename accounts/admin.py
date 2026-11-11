from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import User 



# Register your models here.



class TaskAdmin (admin.ModelAdmin):
    list_display =['email']
    
    
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active','is_verified')
    list_filter = ('email', 'is_superuser', 'is_active','is_verified')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('group permissions', {
            'fields': ('groups', 'user_permissions'),}),
        
        ('important date', {
            'fields': ('last_login',),}),
        
        ('Authentication', {
            'fields': ('email', 'password'),}),
        
        ('permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser','is_verified'),}),)
    
    add_fieldsets = ((None, {'classes': ('wide',),
        'fields':('email','password1','password2','is_staff', 'is_active','is_superuser','is_verified'),}),)
    

admin.site.register(User, CustomUserAdmin)