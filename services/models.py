from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    subtitle = models.CharField(max_length=255, verbose_name='Subtítutlo')
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='services', verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created_at", "updated_at"]

    def __str__(self):
        return self.title
