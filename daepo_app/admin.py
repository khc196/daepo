from django.contrib import admin
from .models import Thing, Chat, Request, Tackle

# Register your models here.
admin.site.register(Thing)
admin.site.register(Chat)
admin.site.register(Request)
admin.site.register(Tackle)
