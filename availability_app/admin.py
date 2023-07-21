from django.contrib import admin
from availability_app.models import EmployeeAvailability, EmployeeSignet

# from myapp.models import Author
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Author, AuthorAdmin)

class EmployeeAvailabilityAdmin(admin.ModelAdmin):
    pass

class EmployeeSignetAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmployeeSignet, EmployeeSignetAdmin)
admin.site.register(EmployeeAvailability, EmployeeAvailabilityAdmin)
