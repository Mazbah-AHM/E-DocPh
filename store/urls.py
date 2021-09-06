from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.shop, name='store',),
    path('brand/<str:id>', views.Brand, name='brand',),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('productdetail/<str:pd_id>', views.productDetail, name='productdetail'),
    path('registration/', views.RegistrationPage, name='registration'),
    path('logoutu/', views.logoutUser, name='logoutu'),
    path('logout1/', views.logoutUser1, name='logout1'),

    path('welcomeu/', views.welcomeUser, name = "welcomeu"),

    path('presup/<int:id>', views.presUp, name='presup'),

    path('updatepres/<int:id>', views.updatePres, name="updatepres"),
    path('editpres/<int:id>', views.editPres, name="editpres"),


    path('loginpatient/', views.LoginPage, name="loginpatient"),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),

    path('order_complete/',views.OrderComplete, name = 'order_complete'),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="store/password_reset.html"), 
    name = "reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="store/password_reset_sent.html"), 
    name = "password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="store/password_reset_form.html"), 
    name="password_reset_confirm"),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="store/password_reset_done.html"), 
    name = "password_reset_complete"),


    # path('init/', views.init, name='init'),
]