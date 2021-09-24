from django.contrib import admin
from .models import Profile,Post,Health ,Police,NeighbourHood,Business
# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Police)
admin.site.register(Health)

