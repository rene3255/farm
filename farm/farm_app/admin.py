from django.contrib import admin
from .models import Breed, Rabbit, Diary, Supply

admin.site.register(Breed)
admin.site.register(Rabbit)
admin.site.register(Supply)
admin.site.register(Diary)


# Register your models here.
