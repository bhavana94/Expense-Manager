from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from . import views

app_name = 'expense'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^manager/', views.helloworld, name="expense"),
    url(r'^credit/', views.credit, name="credit"),
    url(r'^debit/', views.debit, name="debit"),
    url(r'^history/', views.history, name="history"),


]
