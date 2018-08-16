from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView


from .views import records, export_data_excel

urlpatterns = [
    path("records/", records, name="records"),
    path("", RedirectView.as_view(url="/records/")),
    path("login/", admin.site.login, name="login"),
    url("export/xls/$", export_data_excel, name='export')
]
