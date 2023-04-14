from django.urls import path
from . import views

urlpatterns =[
    #path("", views.formview, name="index"),
    path("", views.search_view, name='search_view'),
    path("exchange/",views.exchange_view,name='exchange_view')
]