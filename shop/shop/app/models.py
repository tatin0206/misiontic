from django.db import models

# Create your models here.


class Producto(models.Model):
    name = models.CharField(max_length=50,default="", unique=True)
    description = models.TextField(default="")
    stock = models.PositiveIntegerField(default=0)
    value = models.DecimalField(default=0)

    def __str__(self):
        return self.name


    class meta:
        verbose_name = 'Producto'
        verbodes_name_plural = 'Productos'
        ordering = ['id']
        db_table = 'Productos'
