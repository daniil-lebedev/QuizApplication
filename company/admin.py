from django.contrib import admin
from .models import Team, TeamAdmin, Member

# Register your models here.

admin.site.register(Team)
admin.site.register(TeamAdmin)
admin.site.register(Member)
