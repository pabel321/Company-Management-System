from django.contrib import admin

from .models import about, client
from .models import slider
from .models import client

admin.site.register(about)
admin.site.register(slider)
admin.site.register(client)