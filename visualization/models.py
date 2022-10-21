# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Csi300(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    trade = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csi_300'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Dji(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dji'


class DjiChart(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)
    day_points = models.FloatField(blank=True, null=True)
    hour = models.FloatField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    mid_points = models.FloatField(blank=True, null=True)
    clmov = models.FloatField(blank=True, null=True)
    clmov_s = models.FloatField(blank=True, null=True)
    rho_sigma = models.FloatField(blank=True, null=True)
    s_mov = models.FloatField(blank=True, null=True)
    rho_trend = models.FloatField(blank=True, null=True)
    rho_trend2 = models.FloatField(blank=True, null=True)
    t_mov = models.FloatField(blank=True, null=True)
    bsmov = models.FloatField(blank=True, null=True)
    down1 = models.FloatField(blank=True, null=True)
    up1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dji_chart'


class Ixic(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ixic'


class IxicChart(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)
    day_points = models.FloatField(blank=True, null=True)
    hour = models.FloatField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    mid_points = models.FloatField(blank=True, null=True)
    clmov = models.FloatField(blank=True, null=True)
    clmov_s = models.FloatField(blank=True, null=True)
    rho_sigma = models.FloatField(blank=True, null=True)
    s_mov = models.FloatField(blank=True, null=True)
    rho_trend = models.FloatField(blank=True, null=True)
    rho_trend2 = models.FloatField(blank=True, null=True)
    t_mov = models.FloatField(blank=True, null=True)
    bsmov = models.FloatField(blank=True, null=True)
    down1 = models.FloatField(blank=True, null=True)
    up1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ixic_chart'


class Ndx(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx'


class NdxChart(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)
    day_points = models.FloatField(blank=True, null=True)
    hour = models.FloatField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    mid_points = models.FloatField(blank=True, null=True)
    clmov = models.FloatField(blank=True, null=True)
    clmov_s = models.FloatField(blank=True, null=True)
    rho_sigma = models.FloatField(blank=True, null=True)
    s_mov = models.FloatField(blank=True, null=True)
    rho_trend = models.FloatField(blank=True, null=True)
    rho_trend2 = models.FloatField(blank=True, null=True)
    t_mov = models.FloatField(blank=True, null=True)
    bsmov = models.FloatField(blank=True, null=True)
    down1 = models.FloatField(blank=True, null=True)
    up1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_chart'


class NdxFuture(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_future'


class NdxFuture2(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_future2'


class NdxFuture3(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_future3'


class NdxFutureChart(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)
    day_points = models.FloatField(blank=True, null=True)
    hour = models.FloatField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    mid_points = models.FloatField(blank=True, null=True)
    clmov = models.FloatField(blank=True, null=True)
    clmov_s = models.FloatField(blank=True, null=True)
    rho_sigma = models.FloatField(blank=True, null=True)
    s_mov = models.FloatField(blank=True, null=True)
    rho_trend = models.FloatField(blank=True, null=True)
    rho_trend2 = models.FloatField(blank=True, null=True)
    t_mov = models.FloatField(blank=True, null=True)
    bsmov = models.FloatField(blank=True, null=True)
    down1 = models.FloatField(blank=True, null=True)
    up1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_future_chart'


class NdxFutureChart2(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)
    day_points = models.FloatField(blank=True, null=True)
    hour = models.FloatField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    mid_points = models.FloatField(blank=True, null=True)
    clmov = models.FloatField(blank=True, null=True)
    clmov_s = models.FloatField(blank=True, null=True)
    rho_sigma = models.FloatField(blank=True, null=True)
    s_mov = models.FloatField(blank=True, null=True)
    rho_trend = models.FloatField(blank=True, null=True)
    rho_trend2 = models.FloatField(blank=True, null=True)
    t_mov = models.FloatField(blank=True, null=True)
    bsmov = models.FloatField(blank=True, null=True)
    down1 = models.FloatField(blank=True, null=True)
    up1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_future_chart2'


class NdxFutureChart3(models.Model):
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(blank=True, null=True)
    bsadf_45_1 = models.FloatField(blank=True, null=True)
    bsadf_45_2 = models.FloatField(blank=True, null=True)
    bsadf_45_3 = models.FloatField(blank=True, null=True)
    bsadf_45_4 = models.FloatField(blank=True, null=True)
    bsadf_45_5 = models.FloatField(blank=True, null=True)
    rho_45 = models.FloatField(blank=True, null=True)
    bsadf_mi = models.FloatField(blank=True, null=True)
    day_points = models.FloatField(blank=True, null=True)
    hour = models.FloatField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    mid_points = models.FloatField(blank=True, null=True)
    clmov = models.FloatField(blank=True, null=True)
    clmov_s = models.FloatField(blank=True, null=True)
    rho_sigma = models.FloatField(blank=True, null=True)
    s_mov = models.FloatField(blank=True, null=True)
    rho_trend = models.FloatField(blank=True, null=True)
    rho_trend2 = models.FloatField(blank=True, null=True)
    t_mov = models.FloatField(blank=True, null=True)
    bsmov = models.FloatField(blank=True, null=True)
    down1 = models.FloatField(blank=True, null=True)
    up1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ndx_future_chart3'
