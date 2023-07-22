from django.contrib import admin
from availability_app.models import Employee, EmployeeAvailabilitySignet, EmployeeAvailability, SimpleSignoff

# from myapp.models import Author
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Author, AuthorAdmin)

class EmployeeSignetAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmployeeAvailabilitySignet, EmployeeSignetAdmin)


class EmployeeAvailabilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmployeeAvailability, EmployeeAvailabilityAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)
