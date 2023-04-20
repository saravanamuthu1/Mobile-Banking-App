from django.urls import path
from . import views

urlpatterns =[
    path("", views.search_view, name='search_view'),
    path("exchange/",views.exchange_view,name='exchange_view'),
    path("stocks/",views.stock_view,name="stock_view"),
    path("request/",views.request_view,name="request_view"),
    path("sendmoney/",views.sendmoney_view,name="sendmoney_view"),
     path("accountactivity/",views.accountactivity_view,name="accountactivity_view"),
]