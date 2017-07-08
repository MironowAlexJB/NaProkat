from django.shortcuts import render
from jb_utils.jb_register import *
from core.models import Settings

# Create your views here.
#login page
@only_not_register
def login_page(request):

    object = {}
    object['get_seo_title'] = Settings.get_seo_title_template("Вход на сайт")
    object['get_meta_description'] =  Settings.get_meta_description()
    object['get_meta_keywords'] = Settings.get_meta_keywords()

    return render(request, 'lk/login.html', locals())

