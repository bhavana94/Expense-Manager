from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

app_name = 'expense'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
