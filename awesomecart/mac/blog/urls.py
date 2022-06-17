from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Blog Home"),
    path('design/',views.design,name="Design"),
]