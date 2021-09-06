from django.shortcuts import render, redirect
from django.contrib import messages

from django.db.models import F, Func, Value, CharField, When, Q, F, Case

from django.db.models.functions import Cast
from django.db.models.fields import DateField, DecimalField, TextField

from django.views.generic import TemplateView

from django.db.models.functions import TruncMonth, datetime
from django.db.models import Count, Sum

from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from doctor.models import *
from store.models import *
from store.decorators import *

from django.shortcuts import render, get_object_or_404, redirect

from .forms import *

from datetime import datetime

from django.db.models.functions import Extract


def registration_view(request):
    """
      Renders Registration Form 
    """
    form = CreateUserForm()
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            messages.success(request, 'Hey ' + username +
                             '! your account was created successfully.')

            form.save()

            return redirect('dashboard')
    context = {'form': form}
    return render(request, "admins/registerAdmins.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("welcomeu")


def logout_view2(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("login")


@unauthenticated_user
def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password!')

    context = {}

    return render(request, 'admins/loginAdmins.html', context)


def account_view(request):
    """
      Renders userprofile page "
    """
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.POST:
        form = AdminUpdateform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "profile Updated")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form = AdminUpdateform(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )
    context['account_form'] = form

    return render(request, "admins/userprofile.html", context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def DashboardAdmins(request):
    order = Prescription.objects.all()
    orders = Prescription.objects.all().order_by('-date_ordered')[:10]
    # orders = Prescription.objects.order_by('-date_ordered')[:5]

    inh = OrderItem.objects.all()
    delivered = order.filter(complete='True').count()
    pending = order.filter(complete='False').count()
    order_count = order.count()

    context = {'order': order, 'order_count': order_count,
               'delivered': delivered, 'pending': pending, 'orders': orders, 'inh': inh}

    return render(request, 'admins/dashboardAdmins.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def chart(request):

    # usertime = User.objects.filter(groups__name = 'patient').values('date_joined').annotate(date_only=Cast('date_joined', DateField()))

    # for i in usertime:
    #     result = i.date_only[1]
    #     print(result)

    # usertime = User.objects.filter(groups__name='patient').values(my_datetime = Cast('date_joined', CharField()))

    # for i in usertime:
    #     i['my_datetime'] = i['my_datetime'].month
    #     print(i)

    # print(usertime)

    # dtm_obj = datetime.strptime(usertime, f'%Y-%m-%dT%H:%M:%S.%f%z')

    # formatted_string = dtm_obj.strftime('%b %d, %Y')
    # print(formatted_string)

    usertime = User.objects.filter(groups__name='patient').values(
        'date_joined').annotate(date_only=Cast('date_joined', DateField()))

    days = []
    for u in usertime:
        u = u['date_only']
        # print(u)
        days.append(u)

    # print(days)

    userdata = User.objects.filter(groups__name='patient').extra(
        {'date_joined': "date(date_joined)"}).values('date_joined').annotate(created_count=Count('id'))

    data = []
    for i in userdata:
        i = i['created_count']
        # print(i)
        data.append(i)

    brData = m_Product.objects.all().values('Brand')

    brUn = unique(brData)

    bran = []

    for j in brData:
        j = j['Brand']
        # print(j)
        bran.append(j)

    brUn = unique(bran)

    brq = m_Product.objects.all().filter(Brand='bran').values('quantity')

    # print(brq)

    # qdata = []

    # for j in brq:

    # usertime = User.objects.filter(groups__name = 'patient').values('date_joined')

    # jack = usertime.annotate(date_only = Extract('date_joined', 'month'))

    # print(jack)

    # print(usertime)

    # .annotate(date_only=Func(F('date_joined'),Value('DD'),function='strftime',output_field=CharField())).values('date_only'))
    # FooBarModel.objects.values(Cast('baz__some_datetime_field', TextField()))

    # month = usertime.strftime("%B")

    # print(month)x

    # print(usertime)
    # print(formatted_string)

    # trans = Prescription.objects.filter().values('date_ordered').order_by('date_ordered')
    # transac = Prescription.objects.all()
    # for i in transac:
    #     result = i.get_cart_total

    # print(result)
    # print(trans)

    jack = unique(days)
    # print('jack', jack)

    sparrow = data

    data = []

    for i in range(len(jack)):
        dicts = {}
        dicts["x"] = jack[i]
        dicts["y"] = sparrow[i]
        data.append(dicts)

    brquantity = brData.values('quantity')

    # print(brquantity)

    final = []

    for j in brquantity:
        j = j['quantity']
        # print(j)
        final.append(j)

    damn = []
    for k in range(len(bran)):
        dicts = {}
        dicts['x'] = bran[k]
        dicts['y'] = final[k]
        damn.append(dicts)

    xyz = unique(damn)

    s = m_Product.objects.values('name').filter(orderitem__isnull=False).annotate(
        total_ordered=Sum('orderitem__quantity')).order_by('name')
    print(s)

    namedata = []
    for i in s:
        i = i['name']
        print(i)
        namedata.append(i)

    quantitydata = []
    for i in s:
        i = i['total_ordered']
        print(i)
        quantitydata.append(i)

    # for i in range(len(s)):
    #     dicts = {}
    #     dicts["x"] = jack[i]
    #     dicts["y"] = sparrow[i]
    #     data.append(dicts)

    products = m_Product.objects.all()

    pres = m_Product.objects.all()
    # print('unique', unique(days))
    context = {'products': products, 'pres': pres,
               'usertime': usertime, 'u': data, 'brun': brUn, 'brq': brq, 'namedata': namedata, 'quantitydata': quantitydata}

    return render(request, "admins/piechart.html", context)

# function to get unique values


def unique(list1):

    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def Customers(request):
    patients = Patient.objects.all()

    context = {'patients': patients}
    return render(request, 'admins/customers.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def addProduct(request):

    bdid = m_Product.objects.all()
    if request.method == "POST":
        form = productForm(request.POST)
        print('dfvfdv')
        if request.method == 'POST':
            form = productForm(request.POST, request.FILES)
            if form.is_valid():
                print('fvfv')
                form.save()
                messages.success(request, 'Product added successfully!')
                return redirect('showproduct')
            else:
                print('fsgvd')
                form = productForm()

    context = {}

    return render(request, 'admins/addProduct.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def showProduct(request):

    showproduct = m_Product.objects.all()
    data = m_Product.objects.all().values('quantity', 'name')
    productq = []
    for i in data:
        i = i['quantity']
        # print(i)
        productq.append(i)

    for j in productq:
        if j < 50:
            pro = m_Product.objects.filter(quantity=j).values('name')

            for k in pro:
                k = k['name']
                print(k)
                messages.warning(
                    request, 'Product quantity is low for ' + '' + str((k)))

            # print(qua)

    context = {'productlist': showproduct}

    return render(request, 'admins/showProduct.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def showPatient(request):

    showpatient = User.objects.all().filter(groups__name='patient')
    context = {'patientlist': showpatient}

    return render(request, 'admins/showPatient.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def showDoctor(request):

    showdoctor = User.objects.all().filter(groups__name='doctor')
    context = {'doctorlist': showdoctor}

    return render(request, 'admins/showdoctor.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def showOrders(request):

    showorder = Prescription.objects.all()
    context = {'patientlist': showorder}

    return render(request, 'admins/showOrders.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def deleteProduct(request, id):

    remove = m_Product.objects.get(id=id)
    remove.delete()
    messages.success(request, 'Product Deleted succesfully!')

    return redirect('showproduct')


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def updateProduct(request, id):

    update = m_Product.objects.get(id=id)
    form = productForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product Updated succesfully!')
        return redirect('showproduct')

    context = {'update': update}
    return render(request, 'admins/updateproduct.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def editProduct(request, id):

    update = m_Product.objects.get(id=id)

    context = {'update': update}

    return render(request, 'admins/updateproduct.html', context)


@login_required(login_url='login')
@allowed_users2(allowed_roles2=['admin'])
def Completed(request, com_id, b_id):

    pres = Prescription.objects.filter(id=com_id)[0]

    # pres = Prescription.objects.filter(id = pres_id)[0]
    print(pres)
    if b_id == 'approved':
        pres.complete = True
        pres.save()
        return redirect('showorders')

    context = {'pres': pres}

    return render(request, 'admins/showOrders.html', context)
