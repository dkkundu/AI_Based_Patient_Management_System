from django.contrib import admin
from .models import (
    Slider, Service, Item,
    Doctor, Expertize, Faq,
    Gallery, Contact, Speciality
)

admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Item)
admin.site.register(Doctor)
admin.site.register(Expertize)
admin.site.register(Faq)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Speciality)

admin.site.site_header = 'PMS Admin'
admin.site.site_title = 'PM-System'
admin.site.index_title = 'PM-System'
