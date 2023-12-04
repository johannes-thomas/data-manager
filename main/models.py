# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import datetime


class UserDateModel(models.Model):
    date_created = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, db_column='created_by', related_name='+')
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(User, on_delete=models.RESTRICT, db_column='modified_by', related_name='+', blank=True, null=True)
    
    class Meta:
        abstract = True
        
    #def save(self, *args, **kwargs):
    #    if self._state.adding:
    #        self.date_created = datetime.datetime.now()
    #    else:
    #        self.date_modified = datetime.datetime.now()
    #    
    #    super(BaseModel, self).save(*args, **kwargs)


class CatalogModel(UserDateModel):
    name = models.CharField(max_length=100)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name


class AssociationModel(models.Model):
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    
    class Meta:
        abstract = True
    
    def clean(self):
        if self.valid_from is not None and self.valid_to is not None and self.valid_from > self.valid_to:
            raise ValidationError({'valid_from': _('Valid from date cannot be greater than valid to date.'), 'valid_to': _('Valid from date cannot be greater than valid to date.')})


class ArticleType(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'article_type'
        ordering = ('name',)


class DocumentType(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'document_type'
        ordering = ('name',)


class LimitType(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'limit_type'
        ordering = ('name',)


class FeeScope(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'fee_scope'
        ordering = ('name',)


class DiscountLevel(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'discount_level'
        ordering = ('name',)


class LicenseType(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'license_type'
        ordering = ('name',)


class SubjectArea(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'subject_area'
        ordering = ('name',)


class Institution(CatalogModel):
    contracts_url = models.CharField(max_length=1000)
    
    class Meta:
        #managed = False
        db_table = 'institution'
        ordering = ('name',)


class ProfessionalSociety(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'professional_society'
        verbose_name_plural = 'professional societies'
        ordering = ('name',)


class Country(CatalogModel):
    class Meta:
        #managed = False
        db_table = 'country'
        verbose_name_plural = 'countries'
        ordering = ('name',)


class Currency(CatalogModel):
    code = models.CharField(max_length=3)
        
    class Meta:
        #managed = False
        db_table = 'currency'
        verbose_name_plural = 'currencies'
        ordering = ('code',)
        
    def __str__(self):
        return self.code


class Publisher(UserDateModel):
    imprint = models.CharField(max_length=100)
    main_publisher = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'publisher'
        ordering = ('imprint',)
        
    def __str__(self):
        return self.imprint


class Journal(CatalogModel):
    pissn = models.CharField(max_length=9, blank=True, null=True)
    eissn = models.CharField(max_length=9, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, db_column='country', blank=True, null=True)
    publisher = models.ManyToManyField('Publisher', through='JournalToPublisher')
    professional_society = models.ManyToManyField('ProfessionalSociety', through='JournalToProfessionalSociety')
    subject_area = models.ManyToManyField('SubjectArea', through='JournalToSubjectArea')
    license_type = models.ManyToManyField('LicenseType', through='JournalToLicenseType')
    remark = models.CharField(max_length=1000, blank=True, null=True)
    
    class Meta:
        #managed = False
        db_table = 'journal'
        ordering = ('name',)


class JournalToPublisher(AssociationModel):
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal')
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='publisher')
    
    class Meta:
        #managed = False
        db_table = 'journal_to_publisher'


class JournalToSubjectArea(AssociationModel):
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal')
    subject_area = models.ForeignKey('SubjectArea', models.DO_NOTHING, db_column='subject_area')
    
    class Meta:
        #managed = False
        db_table = 'journal_to_subject_area'


class JournalToProfessionalSociety(AssociationModel):
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal')
    professional_society = models.ForeignKey('ProfessionalSociety', models.DO_NOTHING, db_column='professional_society')
    
    class Meta:
        #managed = False
        db_table = 'journal_to_professional_society'


class JournalToLicenseType(AssociationModel):
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal')
    license_type = models.ForeignKey('LicenseType', models.DO_NOTHING, db_column='license_type')
    
    class Meta:
        #managed = False
        db_table = 'journal_to_license_type'


class Contract(AssociationModel, UserDateModel):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=500, blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='publisher')
    institution = models.ForeignKey('Institution', models.DO_NOTHING, db_column='institution')
    
    class Meta:
        #managed = False
        db_table = 'contract'
    
    def __str__(self):
        return self.number


class Discount(UserDateModel):
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal')
    with_contract = models.BooleanField(blank=True, null=True)
    contract = models.ForeignKey('Contract', models.DO_NOTHING, db_column='contract', blank=True, null=True)
    discount_level = models.ForeignKey('DiscountLevel', models.DO_NOTHING, db_column='discount_level')
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Discount [%]')
    remark = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'discount'


class Fee(UserDateModel):
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal')
    article_type = models.ForeignKey('ArticleType', models.DO_NOTHING, db_column='article_type', blank=True, null=True)
    document_type = models.ForeignKey('DocumentType', models.DO_NOTHING, db_column='document_type', blank=True, null=True)
    license_type = models.ForeignKey('LicenseType', models.DO_NOTHING, db_column='license_type', blank=True, null=True)
    membership = models.BooleanField(blank=True, null=True)
    with_contract = models.BooleanField(blank=True, null=True)
    contract = models.ForeignKey('Contract', models.DO_NOTHING, db_column='contract', blank=True, null=True)
    foreign_author = models.BooleanField(blank=True, null=True)
    fee_scope = models.ForeignKey('FeeScope', models.DO_NOTHING, db_column='fee_scope', blank=True, null=True)
    fee_type = models.CharField(max_length=20, blank=True, null=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2)
    factor = models.PositiveIntegerField(blank=True, null=True)
    lower_limit = models.PositiveIntegerField(blank=True, null=True)
    upper_limit = models.PositiveIntegerField(blank=True, null=True)
    limit_type = models.ForeignKey('LimitType', models.DO_NOTHING, db_column='limit_type', blank=True, null=True)
    currency = models.ForeignKey('Currency', models.DO_NOTHING, db_column='currency')
    valid_from = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'fee'
    
    def clean(self):
        if self.lower_limit is not None and self.upper_limit is not None and self.lower_limit > self.upper_limit:
            raise ValidationError({'lower_limit': _('Lower limit cannot be greater than upper limit.'), 'upper_limit': _('Lower limit cannot be greater than upper limit.')})
    
    def save(self, *args, **kwargs):
        if not self.with_contract:
            self.contract = None
        
        super(Fee, self).save(*args, **kwargs)