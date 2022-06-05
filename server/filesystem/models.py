from django.db import models


class FileTypes(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class FileStructure(models.Model):
    name = models.CharField(max_length=100)
    file_type = models.ForeignKey("filesystem.FileTypes", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name="parents_file", default=None)

    def __str__(self):
        return f'{self.name} (type: {self.file_type}), parent: {self.parent}'
