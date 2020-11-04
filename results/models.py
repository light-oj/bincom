# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now
from django.urls import reverse


class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.ForeignKey("PollingUnit", on_delete=models.CASCADE, db_column='pollingunit_uniqueid')

    class Meta:
        db_table = 'agentname'

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now, editable=False)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_lga_results'

    def __str__(self):
        return self.lga_name


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.ForeignKey("PollingUnit", on_delete=models.CASCADE, db_column='polling_unit_uniqueid')
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now, editable=False)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_pu_results'
        ordering = ('polling_unit_uniqueid',)

    def __str__(self):
        return self.polling_unit_uniqueid.polling_unit_name

    def get_absolute_url(self):
        return reverse("results:polling_unit_result_detail", args=[self.result_id])
    


class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now, editable=False)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_state_results'

    def __str__(self):
        return self.state_name


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now, editable=False)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_ward_results'

    def __str__(self):
        return self.ward_name


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.ForeignKey("States", on_delete=models.CASCADE, db_column='state_id')
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now, editable=False)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'lga'

    def __str__(self):
        return self.lga_name


class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    class Meta:
        db_table = 'party'

    def __str__(self):
        return self.partyname


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.ForeignKey("Ward", on_delete=models.CASCADE, db_column='ward_id')
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE, db_column='lga_id')
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(default=now, editable=False, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'polling_unit'

    def __str__(self):
        return self.polling_unit_name


class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'states'

    def __str__(self):
        return self.state_name


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE, db_column='lga_id')
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(default=now, editable=False)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'ward'

    def __str__(self):
        return self.ward_name
