# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


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


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CompaniesCar(models.Model):
    id = models.BigAutoField(primary_key=True)
    licence_plate = models.CharField(max_length=50)
    company = models.ForeignKey('CompaniesCompany', models.DO_NOTHING)
    date_created = models.DateTimeField()
    date_edited = models.DateTimeField()
    brand = models.CharField(max_length=1000)
    vin = models.CharField(max_length=10000)
    ctc = models.CharField(max_length=10000)
    have_fines = models.IntegerField()
    need_check_fines = models.BooleanField()
    need_check_passes = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'companies_car'


class CompaniesCarfine(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_decis = models.DateTimeField()
    koap_code = models.CharField(max_length=50000)
    koap_text = models.CharField(max_length=50000)
    num_post = models.CharField(max_length=50000)
    date_post = models.DateField()
    date_ssp = models.DateField(blank=True, null=True)
    update_date = models.DateTimeField()
    car = models.ForeignKey(CompaniesCar, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'companies_carfine'


class CompaniesCarpass(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=50)
    status = models.IntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    stop_date = models.DateTimeField(blank=True, null=True)
    cancelled_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000)
    update_date = models.DateTimeField()
    allowed_zone = models.ForeignKey('CompaniesCarpassallowedzone', models.DO_NOTHING)
    car = models.ForeignKey(CompaniesCar, models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey('CompaniesCarpassperiod', models.DO_NOTHING)
    system_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'companies_carpass'

    @property
    def days_left(self):
        date_now = datetime.now()
        days_left = int((self.stop_date - date_now).total_seconds() // (60 * 60 * 24))
        return days_left


class CompaniesCarpassallowedzone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'companies_carpassallowedzone'


class CompaniesCarpassperiod(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'companies_carpassperiod'


class CompaniesCarpasstype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'companies_carpasstype'


class CompaniesComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    date_created = models.DateTimeField()
    company = models.ForeignKey('CompaniesCompany', models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    system = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'companies_comment'


class CompaniesCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    inn = models.CharField(max_length=12)
    status = models.IntegerField()
    date = models.DateField()
    address = models.CharField(max_length=200)
    city = models.ForeignKey('RegionsCity', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('RegionsRegion', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    bank_name = models.CharField(max_length=10000)
    bic = models.CharField(max_length=10000)
    date_created = models.DateTimeField()
    date_edited = models.DateTimeField()
    face = models.CharField(max_length=10000)
    fio = models.CharField(max_length=10000)
    fio_short = models.CharField(max_length=10000)
    k_number = models.CharField(max_length=10000)
    kpp = models.CharField(max_length=10000)
    mail_address = models.CharField(max_length=10000)
    ogrn = models.CharField(max_length=10000)
    osn = models.CharField(max_length=10000)
    r_number = models.CharField(max_length=10000)
    type = models.IntegerField()
    fio_rp = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'companies_company'


class CompaniesCompanydetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10000)
    address = models.CharField(max_length=10000)
    mail_address = models.CharField(max_length=10000)
    inn = models.CharField(max_length=10000)
    kpp = models.CharField(max_length=10000)
    r_number = models.CharField(max_length=10000)
    k_number = models.CharField(max_length=10000)
    bank_name = models.CharField(max_length=10000)
    bic = models.CharField(max_length=10000)
    ogrn = models.CharField(max_length=10000)
    face = models.CharField(max_length=10000)
    osn = models.CharField(max_length=10000)
    fio = models.CharField(max_length=10000)
    fio_short = models.CharField(max_length=10000)
    date_created = models.DateTimeField()
    date_edited = models.DateTimeField()
    city = models.ForeignKey('RegionsCity', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(CompaniesCompany, models.DO_NOTHING)
    type = models.IntegerField()
    fio_rp = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'companies_companydetail'


class CompaniesContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=254)
    company = models.ForeignKey(CompaniesCompany, models.DO_NOTHING)
    date_created = models.DateTimeField()
    date_edited = models.DateTimeField()
    notify = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'companies_contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


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


class DocumentsAct(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=10000)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    datetime_created = models.DateTimeField()
    pdf_scan = models.CharField(max_length=100, blank=True, null=True)
    pdf_with_print = models.CharField(max_length=100, blank=True, null=True)
    to_update = models.BooleanField()
    word_with_print = models.CharField(max_length=100, blank=True, null=True)
    word_without_print = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_act'


class DocumentsAdditionalagreement(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField()
    datetime_created = models.DateTimeField()
    with_tech_task = models.BooleanField()
    word_without_print = models.CharField(max_length=100, blank=True, null=True)
    word_with_print = models.CharField(max_length=100, blank=True, null=True)
    pdf_with_print = models.CharField(max_length=100, blank=True, null=True)
    pdf_scan = models.CharField(max_length=100, blank=True, null=True)
    to_update = models.BooleanField()
    act = models.OneToOneField(DocumentsAct, models.DO_NOTHING, blank=True, null=True)
    bill = models.OneToOneField('DocumentsBill', models.DO_NOTHING, blank=True, null=True)
    contract = models.ForeignKey('DocumentsContract', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'documents_additionalagreement'


class DocumentsAdditionalagreementItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    additionalagreement = models.ForeignKey(DocumentsAdditionalagreement, models.DO_NOTHING)
    item = models.ForeignKey('DocumentsItem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'documents_additionalagreement_items'
        unique_together = (('additionalagreement', 'item'),)


class DocumentsBill(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=10000)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    datetime_created = models.DateTimeField()
    status = models.IntegerField()
    pdf_with_print = models.CharField(max_length=100, blank=True, null=True)
    to_update = models.BooleanField()
    word_with_print = models.CharField(max_length=100, blank=True, null=True)
    word_without_print = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_bill'


class DocumentsContract(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(unique=True, max_length=10000)
    datetime_created = models.DateTimeField()
    company_name = models.CharField(max_length=10000)
    company_address = models.CharField(max_length=10000)
    company_mail_address = models.CharField(max_length=10000)
    company_city = models.CharField(max_length=10000)
    company_inn = models.CharField(max_length=10000)
    company_kpp = models.CharField(max_length=10000)
    company_r_number = models.CharField(max_length=10000)
    company_k_number = models.CharField(max_length=10000)
    company_bank_name = models.CharField(max_length=10000)
    company_bic = models.CharField(max_length=10000)
    company_ogrn = models.CharField(max_length=10000)
    company_face = models.CharField(max_length=10000)
    company_osn = models.CharField(max_length=10000)
    company_fio = models.CharField(max_length=10000)
    company_fio_short = models.CharField(max_length=10000)
    self_name = models.CharField(max_length=10000)
    self_address = models.CharField(max_length=10000)
    self_mail_address = models.CharField(max_length=10000)
    self_city = models.CharField(max_length=10000)
    self_inn = models.CharField(max_length=10000)
    self_kpp = models.CharField(max_length=10000)
    self_r_number = models.CharField(max_length=10000)
    self_k_number = models.CharField(max_length=10000)
    self_bank_name = models.CharField(max_length=10000)
    self_bic = models.CharField(max_length=10000)
    self_ogrn = models.CharField(max_length=10000)
    self_face = models.CharField(max_length=10000)
    self_osn = models.CharField(max_length=10000)
    self_fio = models.CharField(max_length=10000)
    self_fio_short = models.CharField(max_length=10000)
    company = models.ForeignKey(CompaniesCompany, models.DO_NOTHING)
    pdf_scan = models.CharField(max_length=100, blank=True, null=True)
    pdf_with_print = models.CharField(max_length=100, blank=True, null=True)
    word_with_print = models.CharField(max_length=100, blank=True, null=True)
    word_without_print = models.CharField(max_length=100, blank=True, null=True)
    print = models.CharField(max_length=100, blank=True, null=True)
    to_update = models.BooleanField()
    agreements_last_number = models.IntegerField()
    company_details = models.TextField()
    self_details = models.TextField()
    company_fio_rp = models.CharField(max_length=10000)
    self_fio_rp = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'documents_contract'


class DocumentsItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    car = models.ForeignKey(CompaniesCar, models.DO_NOTHING)
    car_pass_allowed_zone = models.ForeignKey(CompaniesCarpassallowedzone, models.DO_NOTHING)
    car_pass_period = models.ForeignKey(CompaniesCarpassperiod, models.DO_NOTHING)
    car_pass_type = models.ForeignKey(CompaniesCarpasstype, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'documents_item'


class DocumentsSelfdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10000)
    address = models.CharField(max_length=10000)
    mail_address = models.CharField(max_length=10000)
    inn = models.CharField(max_length=10000)
    kpp = models.CharField(max_length=10000)
    r_number = models.CharField(max_length=10000)
    k_number = models.CharField(max_length=10000)
    bank_name = models.CharField(max_length=10000)
    bic = models.CharField(max_length=10000)
    ogrn = models.CharField(max_length=10000)
    face = models.CharField(max_length=10000)
    osn = models.CharField(max_length=10000)
    fio = models.CharField(max_length=10000)
    fio_short = models.CharField(max_length=10000)
    prefix = models.CharField(unique=True, max_length=20)
    print = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.BooleanField()
    date_created = models.DateTimeField()
    date_edited = models.DateTimeField()
    city = models.ForeignKey('RegionsCity', models.DO_NOTHING, blank=True, null=True)
    last_number = models.IntegerField()
    type = models.IntegerField()
    fio_rp = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'documents_selfdetail'


class HistorySimplehistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'history_simplehistory'


class PermsPermsgroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sales_department_perms = models.OneToOneField('PermsSalesdepartmentperms', models.DO_NOTHING, blank=True, null=True)
    system_perms = models.OneToOneField('PermsSystemperms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perms_permsgroup'


class PermsPermsgroupManagedGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_permsgroup = models.ForeignKey(PermsPermsgroup, models.DO_NOTHING)
    to_permsgroup = models.ForeignKey(PermsPermsgroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'perms_permsgroup_managed_groups'
        unique_together = (('from_permsgroup', 'to_permsgroup'),)


class PermsSalesdepartmentcompanyperms(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_access = models.BooleanField()
    company_can_create = models.BooleanField()
    company_can_update = models.BooleanField()
    company_can_delete = models.BooleanField()
    company_date_can_update = models.BooleanField()
    company_status_can_update = models.BooleanField()
    comment_access = models.BooleanField()
    car_access = models.BooleanField()
    comment_can_update = models.BooleanField()
    comment_can_delete = models.BooleanField()
    contact_can_create = models.BooleanField()
    contact_can_update = models.BooleanField()
    contact_can_delete = models.BooleanField()
    car_can_create = models.BooleanField()
    car_can_delete = models.BooleanField()
    access = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'perms_salesdepartmentcompanyperms'


class PermsSalesdepartmentperms(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_perms = models.OneToOneField(PermsSalesdepartmentcompanyperms, models.DO_NOTHING, blank=True, null=True)
    access_type = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'perms_salesdepartmentperms'


class PermsSystemgroupperms(models.Model):
    id = models.BigAutoField(primary_key=True)
    can_create = models.BooleanField()
    access = models.BooleanField()
    can_update = models.BooleanField()
    can_delete = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'perms_systemgroupperms'


class PermsSystemperms(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_perms = models.OneToOneField(PermsSystemgroupperms, models.DO_NOTHING, blank=True, null=True)
    user_perms = models.OneToOneField('PermsSystemuserperms', models.DO_NOTHING, blank=True, null=True)
    access_type = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'perms_systemperms'


class PermsSystemuserperms(models.Model):
    id = models.BigAutoField(primary_key=True)
    can_create = models.BooleanField()
    access = models.BooleanField()
    can_update = models.BooleanField()
    can_delete = models.BooleanField()
    can_ban = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'perms_systemuserperms'


class RegionsCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    full_name = models.CharField(max_length=5000)
    region = models.ForeignKey('RegionsRegion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions_city'


class RegionsCountry(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'regions_country'


class RegionsFederaldistrict(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(RegionsCountry, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions_federaldistrict'


class RegionsRegion(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    country = models.ForeignKey(RegionsCountry, models.DO_NOTHING, blank=True, null=True)
    timezone = models.ForeignKey('RegionsTimezone', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions_region'


class RegionsTimezone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'regions_timezone'


class RegionsType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_full = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regions_type'


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class UsersPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    sd_access_type = models.IntegerField()
    user_access_type = models.IntegerField()
    user_can_create = models.BooleanField()
    user_can_update = models.BooleanField()
    user_can_destroy = models.BooleanField()
    user_can_ban = models.BooleanField()
    user_can_update_password = models.BooleanField()
    system_access_type = models.IntegerField()
    sd_contract_can_destroy = models.BooleanField()
    sd_additional_agreement_can_destroy = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users_position'


class UsersPositionUserManagedGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_position = models.ForeignKey(UsersPosition, models.DO_NOTHING)
    to_position = models.ForeignKey(UsersPosition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_position_user_managed_groups'
        unique_together = (('from_position', 'to_position'),)


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    current_pass = models.CharField(max_length=1000)
    email = models.CharField(max_length=254)
    contact_phone = models.CharField(max_length=128)
    contact_email = models.CharField(max_length=254)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    full_name = models.CharField(max_length=400)
    passport_series = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=15)
    passport_issued = models.CharField(max_length=100)
    passport_date = models.DateField(blank=True, null=True)
    passport_code = models.CharField(max_length=10)
    is_admin = models.BooleanField()
    is_banned = models.BooleanField()
    position = models.ForeignKey(UsersPosition, models.DO_NOTHING, blank=True, null=True)
    perms_group = models.ForeignKey(PermsPermsgroup, models.DO_NOTHING, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
