from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.DashboardAdmins, name='dashboard'),

    path('addproduct/', views.addProduct, name='addproduct'),

    path('showproduct/', views.showProduct, name='showproduct'),
    path('showpatient/', views.showPatient, name='showpatient'),
    path('showdoctor/', views.showDoctor, name='showdoctor'),
    path('showorders/', views.showOrders, name='showorders'),
    path('deleteproduct/<int:id>', views.deleteProduct, name="deleteproduct"),

    path('updateproduct/<int:id>', views.updateProduct, name="updateproduct"),
    path('editproduct/<int:id>', views.editProduct, name="editproduct"),

    path('completed/<int:com_id>/<str:b_id>',views.Completed, name = "completed"),

    path('register/',views.registration_view, name="register" ),
    path('logout/',views.logout_view, name="logout" ),

    path('logout2/',views.logout_view2, name="logout2" ),
    
    path('login/',views.login_view, name="login" ),
    path('profile/',views.account_view, name="account" ),

    path('patients/',views.Customers, name='patients'),

    path('piechart/',views.chart, name='piechart'),
]