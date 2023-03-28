from django.db import models

class Permissions(models.Model):
    Permission = models.TextField()

    class Meta:
        permissions = (
            ('SystemAdmin', 'SystemAdmin'),
            ('SystemUser', 'SystemUser'),
            ('SystemGuest', 'SystemGuest'),
            ('AddPermissions', 'AddPermissions'),
            ('Database', 'Database'),
        )

    def __str__(self):
        return self.Permission

class Settings_fieldnames(models.Model):
    Veld1 = models.CharField(max_length=10)
    Veld2 = models.CharField(max_length=10)
    Veld3 = models.CharField(max_length=10)
    Veld4 = models.CharField(max_length=10)

    def __str__(self):
        return "Updated_Fieldnames"

    class Meta:
        verbose_name_plural = "Settings Field Names"

class Settings_lightnames(models.Model):
    Lamp1 = models.CharField(max_length=10)
    Lamp2 = models.CharField(max_length=10)
    Lamp3 = models.CharField(max_length=10)
    Lamp4 = models.CharField(max_length=10)
    Lamp5 = models.CharField(max_length=10)
    Lamp6 = models.CharField(max_length=10)
    field_id = models.CharField(max_length=50)

    def __str__(self):
        return self.field_id

    class Meta:
        verbose_name_plural = "Lights fields"

class Selecting_fields(models.Model):
    field1_active = models.BooleanField(default = False)
    field2_active = models.BooleanField(default = False)
    field3_active = models.BooleanField(default = False)
    field4_active = models.BooleanField(default = False)
    field5_active = models.BooleanField(default = False)

class LightButton(models.Model):
    Lamp001_bool = models.BooleanField(default = False)
    Lamp002_bool = models.BooleanField(default = False)
    Lamp003_bool = models.BooleanField(default = False)
    Lamp004_bool = models.BooleanField(default = False)
    Lamp005_bool = models.BooleanField(default = False)
    Lamp006_bool = models.BooleanField(default = False)
    Lamp007_bool = models.BooleanField(default = False)
    Lamp008_bool = models.BooleanField(default = False)
    Lamp009_bool = models.BooleanField(default = False)
    Lamp0010_bool = models.BooleanField(default = False)
    Lamp0011_bool = models.BooleanField(default = False)
    Lamp0012_bool = models.BooleanField(default = False)
    Lamp0013_bool = models.BooleanField(default = False)
    Lamp0014_bool = models.BooleanField(default = False)
    Lamp0015_bool = models.BooleanField(default = False)
    Lamp0016_bool = models.BooleanField(default = False)

    def __str__(self):
        return f'LightButton {self.id}'
