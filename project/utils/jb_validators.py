from django.forms import ValidationError
import re

MOBILE_PHONE_PATTERN = r'^(\+7|8) \([0-9]{3,3}\) [0-9]{3,3}\-[0-9]{2,2}\-[0-9]{2,2}$'

#validator mobile phone
def validate_mobile_phone(value):

    if not re.match(MOBILE_PHONE_PATTERN, value):
        raise ValidationError("Введите номер телефона в правильном формате", code = "incorrect")


#price validator
def price_validate(value):

    try:
        if  float(value) <= 0:
            raise ValidationError("Цена должна быть больше нуля",  code = "notprice")
    except:
        pass