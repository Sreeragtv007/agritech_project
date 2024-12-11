from django.contrib import admin
from .models import Farmerdata,Uploadedimage
# Register your models here.


class YourModelAdmin(admin.ModelAdmin):
    # Dynamically generate the list of fields
    def get_list_display(self, request):
        # Get all field names except for the primary key
        return [field.name for field in Farmerdata._meta.get_fields() if field.concrete]

# Register the model and admin class
admin.site.register(Farmerdata, YourModelAdmin)


admin.site.register(Uploadedimage)