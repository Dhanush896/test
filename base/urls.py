from django.urls import path
from . import views

urlpatterns = [
    path('',views.stdisplay,name="stdisplay"),
    path('create',views.stinsert,name="stinsert")
]
