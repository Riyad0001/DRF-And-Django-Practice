from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/',views.checkout,name="checkout"),
    path('payment/',views.payment,name="payment"),
    path('purchase/<tran_id>/<user_id>/', views.purchased, name='purchase'),
    path('orders/',views.view_order,name='orders'),
]
