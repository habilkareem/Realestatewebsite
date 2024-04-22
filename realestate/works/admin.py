from django.contrib import admin
from works.models import Realtor,UserInquiry,Listing,Category

# Register your models here.

admin.site.register(Realtor)
admin.site.register(UserInquiry)
admin.site.register(Listing)
admin.site.register(Category)