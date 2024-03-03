from django.contrib import admin
from . import models as m

admin.site.register(m.Test)
admin.site.register(m.TestUser)
