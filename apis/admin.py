from django.contrib import admin

# Register your models here.

from .models import Message, News, Students, Quotas, Vacancys, Images

admin.site.register(Message)
admin.site.register(News)
admin.site.register(Students)
admin.site.register(Quotas)
admin.site.register(Vacancys)
admin.site.register(Images)
