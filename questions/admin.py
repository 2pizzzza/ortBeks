from django.contrib import admin
from . import models as m

admin.site.register(m.Question)
admin.site.register(m.Answer)
