from django.contrib import admin

from results.models import (
    PollingUnit, 
    Agentname, 
    AnnouncedLgaResults, 
    AnnouncedPuResults,
    Ward,
    Lga,
    )

read_only = 'date'
# Register your models here.
# admin.site.register(PollingUnit)
admin.site.register(AnnouncedLgaResults)
#admin.site.register(AnnouncedPuResults)
admin.site.register(Ward)
admin.site.register(Lga)

@admin.register(PollingUnit)
class PollingUnit(admin.ModelAdmin):
    list_display = ('polling_unit_id', 'ward_id', 'uniquewardid', 'polling_unit_number', 'polling_unit_name',)
    list_filter = ('polling_unit_id', 'polling_unit_number', 'polling_unit_name')
    search_fields = ('polling_unit_id', 'polling_unit_name')
    ordering = ('polling_unit_id', 'polling_unit_name')

@admin.register(AnnouncedPuResults)
class AnnouncedPuResults(admin.ModelAdmin):
    list_display = ('result_id', 'polling_unit_uniqueid', 'party_abbreviation', 'party_score')
    list_filter = ('polling_unit_uniqueid', 'party_abbreviation',)
    search_fields = ('polling_unit_uniqueid', 'party_abbreviation',)
    ordering = ('polling_unit_uniqueid', 'party_abbreviation',)