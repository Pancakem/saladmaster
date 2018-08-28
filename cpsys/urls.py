from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView


from .views import export_data_excel

urlpatterns = [
    path("", admin.site.login, name="login"),
    url("export/xls/$", export_data_excel, name='export')
]
