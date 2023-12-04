from django.contrib import admin
from . import models
from django.db import models as django_models
from django.http import HttpResponseRedirect
import datetime


@admin.register(models.ArticleType, models.Contract, models.Country, models.Currency, models.DiscountLevel, models.DocumentType, models.FeeScope, models.Institution, models.LicenseType, models.LimitType, models.ProfessionalSociety, models.Publisher, models.SubjectArea)
class UserDateAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created', 'created_by', 'date_modified', 'modified_by']
    save_as = True
    
    def save_model(self: django_models.Model, request, obj, form, change):
        #instance = form.save(commit=False)
        #form.save_m2m()
        
        #for jtp in obj.journaltopublisher_set.all():
        #    jtp.date_created = datetime.datetime.now()
        #    jtp.created_by = request.user
        
        if not change:
            obj.date_created = datetime.datetime.now()
            obj.created_by = request.user
        else:
            obj.date_modified = datetime.datetime.now()
            obj.modified_by = request.user
        
        super().save_model(request, obj, form, change)


class JournalToPublisherAdmin(admin.TabularInline):
    model = models.JournalToPublisher
    extra = 1
    fields = ['publisher', 'valid_from', 'valid_to']
    verbose_name = 'publisher'


class JournalToSubjectAreaAdmin(admin.TabularInline):
    model = models.JournalToSubjectArea
    extra = 1
    fields = ['subject_area', 'valid_from', 'valid_to']
    verbose_name = 'subject area'


class JournalToProfessionalSocietyAdmin(admin.TabularInline):
    model = models.JournalToProfessionalSociety
    extra = 1
    fields = ['professional_society', 'valid_from', 'valid_to']
    verbose_name = 'professional society'
    verbose_name_plural = 'professional societies'


class JournalToLicenseTypeAdmin(admin.TabularInline):
    model = models.JournalToLicenseType
    extra = 1
    fields = ['license_type', 'valid_from', 'valid_to']
    verbose_name = 'license type'


@admin.register(models.Journal)
class JournalAdmin(UserDateAdmin, admin.ModelAdmin):
    inlines = (JournalToPublisherAdmin, JournalToSubjectAreaAdmin, JournalToProfessionalSocietyAdmin, JournalToLicenseTypeAdmin)


@admin.register(models.Discount)
class DiscountAdmin(UserDateAdmin, admin.ModelAdmin):
    list_display = ['journal', 'get_publisher', 'discount_level', 'discount']
    list_filter = ['journal', 'discount_level', 'discount']
    ordering = ['journal', 'discount_level', 'discount']
    #search_fields = ['journal__name']
    
    @admin.display(ordering='journal__publisher', description='Publisher')
    def get_publisher(self, obj):
        return ', '.join(map(str, obj.journal.publisher.all()))


@admin.register(models.Fee)
class FeeAdmin(UserDateAdmin, admin.ModelAdmin):
    fields = [
        'journal',
        'article_type',
        'document_type',
        'license_type',
        'membership',
        ('with_contract', 'contract'),
        'foreign_author',
        'fee_scope',
        'fee_type',
        'fee',
        'currency',
        'factor',
        'lower_limit',
        'upper_limit',
        'limit_type',
        'valid_from',
        'remark',
        'date_created',
        'created_by',
        'date_modified',
        'modified_by'
    ]
    list_display = [
        'journal',
        'get_publisher',
        'article_type',
        'document_type',
        'license_type',
        'membership',
        'with_contract',
        'contract',
        'foreign_author',
        'fee_scope',
        'fee_type',
        'fee',
        'currency',
        'factor',
        'lower_limit',
        'upper_limit',
        'limit_type'
    ]
    list_filter = [
        'journal',
        'article_type',
        'document_type',
        'license_type',
        'membership',
        'with_contract',
        'contract',
        'foreign_author',
        'fee_scope',
        'fee_type',
        'currency',
        'limit_type'
    ]
    ordering = [
        'journal',
        'article_type',
        'document_type',
        'license_type',
        'membership',
        'with_contract',
        'contract',
        'foreign_author',
        'fee_scope',
        'fee_type',
        'currency',
        'factor',
        'limit_type',
        'lower_limit',
        'upper_limit'
    ]
    #search_fields = ['journal__name']
    
    @admin.display(ordering='journal__publisher', description='Publisher')
    def get_publisher(self, obj):
        return ', '.join(map(str, obj.journal.publisher.all()))
    
    #class Media:
    #    js = (
            #'//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js', # jquery
    #        'custom.js',
    #    )