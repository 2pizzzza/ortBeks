from django.contrib import admin
from . import models as m

admin.site.register(m.User)
admin.site.register(m.Profile)
