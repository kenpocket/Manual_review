# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SketchfabInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    embed_url = models.TextField(blank=True, null=True)
    viewer_url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    face_count = models.IntegerField(blank=True, null=True)
    vertex_count = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    quad = models.IntegerField(blank=True, null=True)
    triangle = models.IntegerField(blank=True, null=True)
    polygon = models.IntegerField(blank=True, null=True)
    total_triangle = models.IntegerField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    download = models.IntegerField(blank=True, null=True)
    free = models.IntegerField(blank=True, null=True)
    is_check = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sketchfab_info'
