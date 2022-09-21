from django.contrib import admin
from Main.models import Agence
from Main.models import Client
from Main.models import Contact

# Register your models here.
admin.site.register(Agence)
admin.site.register(Client)
admin.site.register(Contact)
