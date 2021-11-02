from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('encrypt',views.encrypt,name="encrypt"),
    path('decrypt',views.decrypt,name="decrypt"),
    path('encrypt_complete',views.encrypt_complete,name="encrypt_complete"),
]