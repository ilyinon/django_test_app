from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.http import HttpResponse
from app1.models import User,Server

class UserAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj is False:
            readonly_fields = ['user_id']
            return readonly_fields
        return []
    readonly_fields = ('user_id',)
#    fields = ['user_desc']
#    readonly_fields = []
#    pass
#    def clean_field_1(self):
#        if self.instance.user_enable:
#            return self.instance.user_id
#        else:
#            return self.cleaned_data.get('user_id')
admin.site.register(User,UserAdmin)
admin.site.register(Server)

# Register your models here.
