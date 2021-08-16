from django.urls import path
from . import views
from store.views import checkout

urlpatterns = [

    path('doctor/', views.Doctors, name='doctor'),
    path('registerdoctor/',views.registration_view, name="registerdoctor" ),
    path('logoutd/',views.logout_view, name="logoutd" ),
    path('logoutd1/',views.logout_view1, name="logoutd1" ),

    path('logindoctor/',views.login_view, name="logindoctor" ),
    path('vieworder/<str:pc_id>',views.viewOrder,name = "vieworder"),
    path('doctorapproval/<int:pres_id>/<str:a_id>',views.Approval, name = "doctorapproval"),

    path('checkout/', views.checkout, name='checkout'),  
]