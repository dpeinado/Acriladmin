import django

from django.contrib.auth.models import User
from django.core.validators import EmailValidator, URLValidator
from django.db import models
from django.utils.datetime_safe import date
from utils.validators import phone_regex_validator, zip_code_regex_validator


class Address(models.Model):
    """
    A simple geographical address.
    """

    interior_number = models.CharField(verbose_name='número interior', max_length=10, blank=True)
    exterior_number = models.CharField(verbose_name='número exterior', max_length=10)
    street = models.CharField(verbose_name='calle', max_length=45)
    town = models.CharField(verbose_name='municipio', max_length=45, blank=True)
    city = models.CharField(verbose_name='ciudad', max_length=45, blank=True)
    state = models.CharField(verbose_name='estado', max_length=45, blank=True)
    country = models.CharField(verbose_name='país', max_length=45, blank=True)
    zip_code = models.CharField(verbose_name='CP', max_length=5, blank=True, validators=[zip_code_regex_validator])

    class Meta:
        verbose_name = 'dirección'
        verbose_name_plural = 'direcciones'

    def __str__(self):
        return "{0}, {1}, {2}".format(self.exterior_number, self.street, self.town)


class EmployeeRole(models.Model):
    """
    Describes a role assigned to an employee.
    """
    ADMINISTRATOR = "Administrador"
    TELEPHONE_SALES = "Ventas telefónicas"
    FIELD_SALES = "Ventas en campo"
    SALES_AGENT = "Agente de ventas"
    INSTALLER = "Instalador"
    DRIVER = "Chofer"
    DOME_PRODUCER = "Productor de domos"
    WAREHOUSE_CHIEF = "Jefe de almacén"
    NAME_CHOICES = (
        (ADMINISTRATOR, ADMINISTRATOR),
        (TELEPHONE_SALES, TELEPHONE_SALES),
        (FIELD_SALES, FIELD_SALES),
        (SALES_AGENT, SALES_AGENT),
        (INSTALLER, INSTALLER),
        (DRIVER, DRIVER),
        (DOME_PRODUCER, DOME_PRODUCER),
        (WAREHOUSE_CHIEF, WAREHOUSE_CHIEF),
    )

    name = models.CharField(verbose_name='nombre del rol', max_length=20, primary_key=True)
    description = models.CharField(verbose_name='descripción del rol', max_length=50)

    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    An employee that works for Acrilfrasa.
    """
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = (
        (MALE, "Masculino"),
        (FEMALE, "Femenino")
    )

    @property
    def full_name(self):
        return "{0} {1} {2}".format(self.name, self.paternal_last_name, self.maternal_last_name).rstrip()

    name = models.CharField(verbose_name='nombre(s)', max_length=20)
    paternal_last_name = models.CharField(verbose_name='apellido paterno', max_length=20)
    maternal_last_name = models.CharField(verbose_name='apellido materno', max_length=20)
    gender = models.PositiveSmallIntegerField(verbose_name='género', choices=GENDER_CHOICES)
    phone = models.CharField(verbose_name='teléfono', max_length=15, blank=True, validators=[phone_regex_validator])
    email = models.EmailField(verbose_name='correo electrónico', blank=True,
                              validators=[EmailValidator(message='Correo electrónico inválido.')])
    picture = models.ImageField(verbose_name='imagen de perfil', blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='dirección', null=True, blank=True)

    number = models.CharField(verbose_name='número', max_length=45, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario del sistema', null=True,
                                blank=True)
    seniority = models.DateField(verbose_name='antigüedad', default=django.utils.timezone.now)
    is_active = models.BooleanField(verbose_name='activo', default=True)
    roles = models.ManyToManyField(EmployeeRole, verbose_name='roles')

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'

    def __str__(self):
        return self.full_name


class Client(models.Model):
    """
    One of Acrilfrasa's clients.
    """

    name = models.CharField(verbose_name='nombre', max_length=45)
    phone = models.CharField(verbose_name='teléfono', max_length=15, blank=True, validators=[phone_regex_validator])
    website = models.URLField(verbose_name='sitio web', max_length=45, blank=True,
                              validators=[URLValidator(message="URL inválida.")])
    email = models.EmailField(verbose_name='correo electrónico', blank=True,
                              validators=[EmailValidator(message="Correo electrónico inválido.")])
    picture = models.ImageField(verbose_name='imagen', blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='dirección', null=True, blank=True)
    client_since = models.DateField(verbose_name='antigüedad', auto_now_add=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
            return self.name


class BranchOffice(models.Model):
    """
    A location involved in the business activities of the firm.
    """
    name = models.CharField(verbose_name='nombre de la sucursal', max_length=45)
    phone = models.CharField(verbose_name='teléfono', max_length=15, blank=True, validators=[phone_regex_validator])
    website = models.URLField(verbose_name='sitio web', max_length=45, blank=True,
                              validators=[URLValidator(message="URL inválida.")])
    email = models.EmailField(verbose_name='correo electrónico', blank=True,
                              validators=[EmailValidator(message="Correo electrónico inválido.")])
    picture = models.ImageField(verbose_name='imagen', blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='dirección', null=True, blank=True)
    administrator = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='administrador de la sucursal',
                                      related_name="administrated_branches",
                                      limit_choices_to=
                                      {
                                          'roles__name': EmployeeRole.ADMINISTRATOR
                                      })
    employees = models.ManyToManyField(Employee, verbose_name='empleados de la sucursal', blank=True)

    class Meta:
        verbose_name = 'sucursal'
        verbose_name_plural = 'sucursales'

    def __str__(self):
        return self.name
