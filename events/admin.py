from django.contrib import admin
from .models import MyClubUser, Venue, Event


admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)

