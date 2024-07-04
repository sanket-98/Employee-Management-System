from django.contrib import admin
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'password', 'confirm_password')

admin.site.register(SignUp, SignUpAdmin)
