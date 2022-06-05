from django.db import models


class FileTypes(models.Model):
    name = models.CharField(max_length=100, unique=True)


class FileStructure(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey("filesystem.FileTypes", on_delete=models.CASCADE)
    child = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, related_name="childs_file")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name="parents_file")
