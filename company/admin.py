from django.contrib import admin
from .models import Company, CompanyAdmin, Worker

# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyAdmin)
admin.site.register(Worker)
