from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from django.views.generic import TemplateView

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage

from .decorators import *

from django.http import JsonResponse
from .models import *
from .forms import *
from .utils import cookieCart, cartData, guestOrder


def RegistrationPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='patient')
            user.groups.add(group)

            messages.success(request, 'Account successfully created for ' + username)

            return redirect('loginpatient')
    context = {'form': form}
    return render(request, 'store/register.html', context)

@unauthenticated_user
def LoginPage(request):

    if request.user.is_authenticated:
        return redirect('store')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('store')
            else:
                messages.error(request, 'Invalid username or password!')

    context = {}

    return render(request, 'store/login.html', context)


@login_required(login_url='loginpatient')
def logoutUser(request):
    logout(request)
    return redirect('welcomeu')

@login_required(login_url='loginpatient')
def logoutUser1(request):
    logout(request)
    return redirect('loginpatient')    


def welcomeUser(request):

    return render(request, 'store/welcome.html')

@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def presUp(request,id):

    context ={'id':id}

    return render(request,'store/prescripUp.html', context)

@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def updatePres(request,id):
    print(id)
    update = Prescription.objects.get(id=id)

    form = presUpForm(request.POST, request.FILES, instance=update)
    if form.is_valid():
        print('fvfv')
        form.save()
        return redirect('store')
    # else:
    #     print('fsgvd')
    #     form = presUpForm()

    context = {'update':update,'form':form}            

    return render(request, 'store/prescripUp.html',context)

@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def editPres(request, id):

    update = Prescription.objects.get(id=id)

    context = {'update': update}

    return render(request, 'admins/prescripUp.html', context)  
      

@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def productDetail(request, pd_id):

    products = m_Product.objects.filter(id=pd_id)

    context = {'products': products}
    

    return render(request, 'store/productDetail.html', context)




def Brand(request, id):

    brand = m_Product.objects.all().values('Brand')

    barbosa = unique(brand)

    prod = m_Product.objects.all().filter(Brand = id)

    print(prod)

    context = {'prod':prod, 'brand': barbosa}

    return render(request, 'store/Brand.html',context)






@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def shop(request):

    data = ShippingAddress.objects.all().values('customer')
    print(data)

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = m_Product.objects.all()

    
    brand = m_Product.objects.all().values('Brand')

    barbosa = unique(brand)

    prod = m_Product.objects.all().filter(Brand = id).values('name')


   

    # print('unique', barbosa)





    p = Paginator(products, 6)

    # print('Number of Pages')
    # print(p.num_pages)

    page_num = request.GET.get('page',1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)    

    context = {'products': page, 'cartItems': cartItems,'brand':barbosa}
    return render(request, 'store/store.html', context)



def unique(list1):

    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def cart(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def OrderComplete(request):

    context = {}
    return render(request, 'store/thankyouPage.html',context)    

@login_required(login_url='loginpatient')
@allowed_users(allowed_roles=['patient'])
def checkout(request):

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user
    product = m_Product.objects.get(id=productId)
    order, created = Prescription.objects.get_or_create(
        patient=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):

    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Prescription.objects.get_or_create(
            patient=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            contact_no=data['shipping']['contact_no']
        )

    return JsonResponse('Payment Processing...', safe=False)
