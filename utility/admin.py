from django.contrib import admin
from .models import User, Groups, Appointments, Note
# Register your models here.

admin.site.register(User)
admin.site.register(Groups)
admin.site.register(Note)
admin.site.register(Appointments)