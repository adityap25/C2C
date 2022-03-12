from django.contrib import admin
from .models import User,TpoProfile,CompanyProfile
# # Register your models here.
admin.site.register(User)
admin.site.register(TpoProfile)
admin.site.register(CompanyProfile)