from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    date = models.CharField(max_length=100, null=False, blank=False)
    document = models.FileField(upload_to='directory/publications_files')

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.name
