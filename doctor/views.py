
from django.core import mail
from django.utils.html import strip_tags
from django.http import request, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import templatize
from . validator import *

from .models import *

from django.shortcuts import render, get_object_or_404, redirect

from .forms import *

from store.models import *
from store.utils import *
from store.views import checkout
from store.decorators import *

# Create your views here.

@login_required(login_url='logindoctor')
@allowed_users1(allowed_roles1=['doctor'])
def Doctors(request):

    showorders = Prescription.objects.all()

    orderdata = Prescription.objects.all().filter(authorize = 'Pending')

    data = Prescription.objects.all().values("precripImage")
    print(data)

    print(orderdata)

    context = {'orderlist': showorders, 'orderdata':orderdata, 'data':data}
    return render(request, 'doctor/doctor.html', context)

@login_required(login_url='logindoctor')
@allowed_users1(allowed_roles1=['doctor'])
def viewOrder(request, pc_id):

    products = Prescription.objects.get(id=pc_id)
    product = products.orderitem_set.all()
    print(product)
    data = Prescription.objects.filter(id = pc_id).values('precripImage')
    print(data)

    

    context = {'product': product, 'products': products,'data':data}
    return render(request, 'doctor/vieworder.html', context)

@login_required(login_url='logindoctor')
@allowed_users1(allowed_roles1=['doctor'])
def Approval(request, pres_id, a_id):

    pres = Prescription.objects.filter(id=pres_id)[0]

    template = render_to_string(
        'doctor/email_template.html', {'name': pres.patient.username})
    template1 = render_to_string(
        'doctor/email_rejected.html', {'name': pres.patient.username})
    print(template)
    print(template1)

    # pres = Prescription.objects.filter(id = pres_id)[0]
    print(pres)
    if a_id == 'approved':
        pres.authorize = "Accepted"
        pres.save()
        # email = EmailMessage(
        # 'Your Order Has been accepted!',
        # template,
        # settings.EMAIL_HOST_USER,
        # [pres.patient.email]

        # )
        # print(pres.patient.email)
        # email.fail_silently = False
        # email.send()
        subject = 'Congratulations! Your order has been approved'
        html_message = render_to_string('doctor/email_template.html')
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = pres.patient.email
        mail.send_mail(subject, plain_message, from_email,[to], html_message=html_message)

        return redirect('doctor')
    elif a_id == 'rejected':
        pres.authorize = "Rejected"
        pres.save()   
        email = EmailMessage(
        'Your Order Has been Rejected!',
        template1,
        settings.EMAIL_HOST_USER,
        [pres.patient.email]
         
        )
        print(pres.patient.email)  
        email.fail_silently = False
        email.send() 
        return redirect('doctor')

    context = {'pres':pres}

    return render(request, 'doctor/vieworder.html', context)


def registration_view(request):


    form = CreateUserForm
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='doctor')
            user.groups.add(group)

            messages.success(request, 'Account successfully created for ' + username)

            form.save()
            
    
            return redirect('doctor')
        
    context = {'form':form}
    return render(request, "doctor/registerDoctor.html", context)



def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("welcomeu")

def logout_view1(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('logindoctor')  


@unauthenticated_user
def login_view(request):

    if request.user.is_authenticated:
        return redirect('doctor')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('doctor')
            else:
                redirect('logindoctor')
                messages.error(request, 'Invalid username or password!')


    context = {}

    return render(request, 'doctor/loginDoctor.html', context)





# @unauthenticated_user
# def login_view(request):
#     """
#       Renders Login Form
#     """
    
#     user = request.user
#     if user.is_authenticated:
#         return redirect("doctor")
#     else:    
#         if request.method == 'POST':
#             # form = AccountAuthenticationForm(request.POST)
            
#             email = request.POST.get('email')
#             print(email)
#             users = Doctor.objects.filter(email=email)
            
#             print(users)
#             if email == users[0].email:
#                 login(request, users[0])
#                 print(users)
#                 messages.success(request, "Logged In")
#                 return redirect("doctor")
#             else:
#                 return redirect("logindoctor")
#         else:
#             redirect('logindoctor')
#             # form = AccountAuthenticationForm()
#             # print(form)

#         context = {'user':user}
#         return render(request, "doctor/loginDoctor.html", context)
 
