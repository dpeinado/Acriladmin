import back_office.models as models
from django.contrib import admin


class AddressAdmin(admin.ModelAdmin):
    """
    Specifies the details for the admin app in regard
    to the Address entity.
    """
    fields = (
        ('street', 'exterior_number'),
        'interior_number',
        ('town', 'city'),
        ('state', 'country'),
        'zip_code'
    )
    list_display = ('town', 'street', 'exterior_number')
    list_filter = ('country', 'state', 'city', 'town')


class EmployeeAdmin(admin.ModelAdmin):
    """
    Specifies the details for the admin app in regard
    to the Employee entity.
    """
    fieldsets = (
        ("Datos personales", {
            'fields': (
                'name', 'paternal_last_name', 'maternal_last_name',
                'gender', 'phone', 'email', 'picture', 'address'
            )
        },),
        ('Datos de empleado', {
            'fields': ('number', 'user', 'seniority', 'is_active', 'role')
        })
    )


class BranchOfficeAdmin(admin.ModelAdmin):
    """
    Specifies the details for the admin app in regard
    to the OfficeBranch entity.
    """
    filter_horizontal = ("employees",)


admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.EmployeeRole)
admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.Client)
admin.site.register(models.BranchOffice, BranchOfficeAdmin)
