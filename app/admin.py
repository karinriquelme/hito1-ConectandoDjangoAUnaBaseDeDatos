from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Comuna)
admin.site.register(Tipo_propiedad)
admin.site.register(Propiedad)
admin.site.register(Region)
admin.site.register(Provincia)

