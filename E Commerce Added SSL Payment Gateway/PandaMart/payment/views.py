from django.shortcuts import render,redirect,HttpResponseRedirect
from order.models import Order,Cart
from sslcommerz_lib import SSLCOMMERZ
import random,string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def checkout(request):
    order_qs=Order.objects.filter(user=request.user,ordered=False)[0]
    order_item=order_qs.orderitems.all()

    order_total=order_qs.get_totals()

    context={
        'order_items':order_item,
        'order_total':order_total
    }
    return render(request,"checkout.html",context)

@login_required
def payment(request):
    
    print('\n==========================')
    print('Payment Called')
    print('==========================\n')

    store_id = 'harun67d414cb1861c'
    #Wrong_id
    # store_id = 'democ66334da1b3c91'
    store_pass = 'harun67d414cb1861c@ssl'
    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    order_total = order_qs[0].get_totals()
    print(order_total)
    # status_url = request.build_absolute_uri(reverse('payment:complete'))
    
    
    settings = {'store_id': store_id,
                'store_pass': store_pass, 'issandbox': True}
    
    
    sslcommez = SSLCOMMERZ(settings)
    print(sslcommez)
    post_body = {}
    post_body['total_amount'] = order_total
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_transaction_id_generator()
    post_body['success_url'] = f'http://127.0.0.1:8000/payment/purchase/{post_body['tran_id']}/{request.user.id}/'
    post_body['fail_url'] = f'http://127.0.0.1:8000/order/cart/{request.user.id}/0/'
    post_body['cancel_url'] = f'http://127.0.0.1:8000/order/cart/{request.user.id}/0/'
    post_body['emi_option'] = 0
    post_body['cus_email'] = request.user.email
    post_body['cus_phone'] = '0178888889' 
    post_body['cus_add1'] = 'Dhaka' 
    post_body['cus_city'] = 'Uttara'
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # OPTIONAL PARAMETERS
    # post_body['value_a'] = id
    # post_body['value_b'] = request.user.id
    # post_body['value_c'] = 'email'

    response = sslcommez.createSession(post_body)
    print(response)




    return redirect(response['GatewayPageURL'])
# @login_required
# def payment(request):
#     order_qs=Order.objects.filter(user=request.user,ordered=False)[0]
#     order_item=order_qs.orderitems.all()

#     order_total=order_qs.get_totals()
         
#     settings = { 'store_id': 'harun67d414cb1861c', 'store_pass': 'harun67d414cb1861c@ssl', 'issandbox': True }
#     sslcz = SSLCOMMERZ(settings)
#     post_body = {}
#     post_body['total_amount'] = order_total
#     post_body['currency'] = "BDT"
#     post_body['tran_id'] = unique_transaction_id_generator()
#     post_body['success_url'] = f"http://127.0.0.1:8000/purchased/{post_body['tran_id']}/{request.user.id}"
#     post_body['fail_url'] = "http://127.0.0.1:8000/order/cart"
#     post_body['cancel_url'] = "http://127.0.0.1:8000/order/cart"
#     post_body['emi_option'] = 0
#     post_body['cus_name'] = request.user.username
#     post_body['cus_email'] = request.user.email
#     post_body['cus_phone'] = "01700000000"
#     post_body['cus_add1'] = "Baridhara"
#     post_body['cus_city'] = "Dhaka"
#     post_body['cus_country'] = "Bangladesh"
#     post_body['shipping_method'] = "NO"
#     post_body['multi_card_name'] = ""
#     post_body['num_of_item'] = 1
#     post_body['product_name'] = "Test"
#     post_body['product_category'] = "Test Category"
#     post_body['product_profile'] = "general"


#     response = sslcz.createSession(post_body) # API response
#     print(response)
#     # Need to redirect user to response['GatewayPageURL']
#     print("Payment Done")
#     return redirect(response['GatewayPageURL'])
# @csrf_exempt
# def purchased(request,tran_id,user_id):
#     print("Now In Purchase")
#     print(f"Request Method: {request.method}")
#     print(f"CSRF Token: {request.META.get('CSRF_COOKIE', 'No Token')}")

#     user=User.objects.get(id=user_id)
#     order_qs=Order.objects.filter(user=user,ordered=False)
#     order=order_qs[0]
#     order.ordered=True
#     order.orderId=tran_id
#     order.paymentId=tran_id

#     cart_item=Cart.objects.filter(user=user,purchased=False)

#     for items in cart_item:
#         items.purchased=True
#         items.save()

#     return HttpResponseRedirect(reverse('payment:orders'))
@csrf_exempt
def purchased(request, tran_id,user_id):
    
    print('\n==========================')
    print('Purcahse Called')
    print('==========================\n')
    
    user=User.objects.get(id=user_id)
    
    print(request.user)
    
    order_qs = Order.objects.filter(user=user, ordered=False)
    print(order_qs)
    order = order_qs[0]
    order.ordered = True
    order.orderId = tran_id
    order.paymentId = tran_id
    order.save()
    cart_items = Cart.objects.filter(user=user, purchased=False)
    print(cart_items)
    for item in cart_items:
        item.purchased = True
        item.save()
    return HttpResponseRedirect(reverse('payment:orders'))
@csrf_exempt
def view_order(request):
    orders=Order.objects.filter(user=request.user,ordered=True)

    if orders:
        context={
            'orders':orders,
        }
    else:
        messages.warning(request,"You Don't Have Any Orders")
    return render(request,"orders.html",context)




    

    


