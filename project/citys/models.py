from django.db import models

# Create your models here.

#clas city
class City(models.Model):

    #name city
    name = models.CharField(verbose_name = "Наименование города", max_length = 100)

    def __str__(self):
        return self.get_name()

    #GETTERS
    def get_name(self):
        return self.name

        
    ####

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"