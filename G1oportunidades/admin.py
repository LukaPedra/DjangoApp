from django.contrib import admin

# Register your models here.


from .models import user

admin.site.register(user)

from .models import vaga

admin.site.register(vaga)