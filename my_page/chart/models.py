from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brands(models.Model):
    company_name = models.CharField(primary_key=True, blank=True, null=True)
    company_size = models.IntegerField(blank=True, null=True)
    company_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'


class BrandsOffice(models.Model):
    slug = models.CharField(primary_key=True, blank=True, null=True)
    company_name = models.CharField(blank=True, null=True)
    office = models.CharField(blank=True, null=True)
    id = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands_office'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmploymentTypes(models.Model):
    id = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    from_salary = models.IntegerField(blank=True, null=True)
    to_salary = models.IntegerField(blank=True, null=True)
    currency = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_types'


class Offers(models.Model):
    id = models.CharField(primary_key=True, blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    marker_icon = models.CharField(blank=True, null=True)
    experience_level = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    country_code = models.CharField(blank=True, null=True)
    remote = models.CharField(blank=True, null=True)
    workplace_type = models.CharField(blank=True, null=True)
    company_name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class Skills(models.Model):
    id = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'
