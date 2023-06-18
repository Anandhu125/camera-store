from django.contrib import admin

# Register your models here.
from cam.models import Camera,Category,SpecialProduct
admin.site.register(Camera)
admin.site.register(Category)
admin.site.register(SpecialProduct)