from django.db import models
from django.contrib.auth.models import User
from utils import jb_validators
from citys.models import City

# Create your models here.

TYPES_OWNER = (
    (0, "Компания"),
    (1, "Частное лицо")
)

#class owner
class Owner(models.Model):

    #user objeect in django system
    user = models.ForeignKey(User, verbose_name = "Объект пользователя", related_name = "owner")
    #fio or name compa
    type_user = models.IntegerField(choices = TYPES_OWNER, default = 1, verbose_name = "Тип владельца")
    #name company or fio owner
    name = models.CharField(verbose_name  = "Наименоване владельца", max_length = 50, help_text = "наименование компании или ФИО владельца")
    #phone number for link
    phone = models.CharField(verbose_name = "Номер мобильного телефона", max_length = 50, validators = [jb_validators.validate_mobile_phone,], help_text = "номер мобильного телефона")
    #true face - check
    trustee = models.BooleanField(verbose_name = "Доверенное лицо", default = False)
    #photo
    photo = models.ImageField(upload_to = "owners/%Y/%m/%d/", verbose_name = "Фотография владельца", blank = True, null = True)
    #city
    city = models.ForeignKey(City, verbose_name = "Город", null = True, on_delete = models.SET_NULL, related_name = "owners")
    #adress
    address = models.CharField(verbose_name = "Адрес", default = "", null = True, blank = True, max_length = 300)
    #settings for map
    coord_x = models.FloatField(verbose_name = "Координата X на карте", help_text = "карта отображается при наличии адреса", null = True, blank = True)
    coord_y = models.FloatField(verbose_name = "Координата Y на карте", help_text = "карта отображается при наличии адреса", null = True, blank = True)

    def __str__(self):
        return self.get_name()

    #GETTERS
    def get_user(self):
        return self.user

    def get_type_user(self):
        return self.type_user

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def is_trustee(self):
        return self.trustee

    def get_photo(self):
        if self.photo:
            return self.photo.url
        return False

    def get_city(self):
        return self.city

    def get_address(self):
        return self.address

    def get_coord_x(self):
        if self.coord_x:
            return self.coord_x
        return 0

    def get_coord_y(self):
        if self.coord_y:
            return self.get_coord_y
        return 0

    ####

    class Meta:
        verbose_name = "владелец"
        verbose_name_plural = "владельцы"

