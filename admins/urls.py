from django.urls import path
from django.contrib.auth import views as auth_views
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

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="admins/password_reset_admins.html"), 
    name = "reset_password_admins"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="admins/password_reset_sent_admins.html"), 
    name = "password_reset_done_admins"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="admins/password_reset_form_admins.html"), 
    name="password_reset_confirm_admins"),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="admins/password_reset_done_admins.html"), 
    name = "password_reset_complete_admins"),
]    