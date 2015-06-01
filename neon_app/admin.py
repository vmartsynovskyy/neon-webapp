from django.contrib import admin
from neon_app.models import Day, Block, Event, About, Staff

# Register your models here.

admin.site.register(Event)
admin.site.register(Block)
admin.site.register(Day)
admin.site.register(About)
admin.site.register(Staff)