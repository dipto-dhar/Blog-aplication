from django.contrib import admin
from django.db import models

from .models import Post,Category,Settings,contacts,about_content

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Settings)
admin.site.register(contacts)
admin.site.register(about_content)

