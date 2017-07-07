from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#type user
TYPE_USER = (
    (0, "Владелец"),
    (1, "Клиент")
)

#model dop user information
class DopUser(models.Model):

    #user
    user = models.ForeignKey(User, verbose_name = "Объект пользователя")
    #type user
    type_user = models.IntegerField(verbose_name = "Тип пользователя", help_text = "у ")