from django.urls import path
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

    # path('init/', views.init, name='init'),
]