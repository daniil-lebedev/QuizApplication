from django.contrib import admin
from .models import Announcement, Comment, AdminComment

admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(AdminComment)
