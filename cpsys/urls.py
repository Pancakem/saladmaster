from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView


from .views import records

urlpatterns = [
    path("records/", records, name="records"),
    #url(r"^download/(.*)", download, name="download"),
    path("", RedirectView.as_view(url="/records/")),
    path("login/", admin.site.login, name="login"),
    #path("upload/", UploadView.as_view()),
]
