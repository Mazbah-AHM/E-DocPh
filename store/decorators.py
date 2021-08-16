from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('logout1')
        return wrapper_func
    return decorator        


def allowed_users1(allowed_roles1=[]):

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles1:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('logoutd1')
        return wrapper_func
    return decorator        


def allowed_users2(allowed_roles2=[]):

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles2:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('logout2')
        return wrapper_func
    return decorator  



def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "patient":
            return redirect('store')
        if group == 'admin':
            return redirect(request, *args, **kwargs)
        if group == 'doctor':
            return redirect('doctor')   

    return wrapper_func