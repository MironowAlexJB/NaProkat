from django.db import models
from owners.models import Owner

# Create your models here.

STATUS_THING = (
    (0, "Занята"),
    (1, "Свободна"),
    (2, "Не указан")
)

#class thing
class Thing(models.Model):

    #owner thing
    owner = models.ForeignKey(Owner, verbose_name = "Владелец", blank = False, null = True, on_delete = models.SET_NULL, related_name = "things")
    #name thing
    name = models.CharField(verbose_name = "Наименование вещи", max_length = 300)
    #description thing
    description = models.TextField(verbose_name = "описание вещи", blank = True, null = True, default = "")
    #photo thing
    photo = models.ImageField(verbose_name = "фотография вещи", upload_to = "things/%Y/%m/%d/")
    #status product
    status = models.IntegerField(verbose_name = "статус заказа", default = 1, choices = STATUS_THING)
    #date free
    date_free = models.DateTimeField(verbose_name = "Занята до...", blank = True, null = True)
    #active
    active = models.BooleanField(verbose_name = "Активная вещь", default = True)

    def __str__(self):
        return self.get_name()

    #GETTERS
    def get_owner(self):
        return self.owner

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_photo(self):
        if self.photo:
            return self.photo.url

    def get_status(self):
        return self.status

    def get_date_free(self):
        return self.strftime("%H:%M %d.%m.%y")

    def is_active(self):
        return self.active

    ####

    class Meta:
        verbose_name = "вещь"
        verbose_name_plural = "вещи"


#photos for thing
class PhotoThing(models.Model):

    thing = models.ForeignKey(Thing, verbose_name = "вещь", related_name = "photos")
    #photo thing
    photo = models.ImageField(verbose_name = "фотография вещи", upload_to = "thingsphotos/%Y/%m/%d/")

    def __str__(self):
        return str(self.thing) + " ID: " + str(self.id)

    class Meta:
        verbose_name = "фотография вещи"
        verbose_name_plural = "фотографии вещей"