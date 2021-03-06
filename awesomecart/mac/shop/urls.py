from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Shop Home"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="Contact"),
    path('tracker/',views.tracker,name="Tracker"),
    path('productview/<int:myid>',views.products,name="Prodview"),
    path('checkout/',views.checkout,name="Checkout"),
    path('test/',views.test,name="Test"),
]