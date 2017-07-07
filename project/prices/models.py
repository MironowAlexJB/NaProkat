from django.db import models
from things.models import Thing


# Create your models here.
#ed payment
class EdPayment(models.Model):

    #name ed payment
    name = models.CharField(verbose_name = "Единица времени", unique = True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "единица времени оплаты"
        verbose_name_plural = "единицы времени оплаты"

#class price for thing
class PriceForThing(models.Model):

    #thing object
    thing = models.ForeignKey(Thing, verbose_name = "вещь", related_name = "prices")
    #price
    price = models.FloatField(verbose_name = "цена", validators = [jb_validators.price_validate, ])
    #ed payment
    ed_price = models.ForeignKey(EdPayment, verbose_name = "единица времени оплаты")

    def __str__(self):
        return str(self.thing) + " по цене " + str(self.get_price()) + " за " + str(self.get_ed_price)

    #GETTERS
    def get_price(self):
        return self.price

    def get_thing(self):
        return self.thing

    def get_ed_price(self):
        return self.ed_price

    ####

    class Meta:
        unique_together = (('thing', 'ed_izm'),)
        verbose_name = "цена проката"
        verbose_name_plural = "цены проката"

