from django.urls import path
from.import views


urlpatterns = [
    
     path('',views.index),
     path('index',views.index,name='index.html'),
     path('addemp',views.addemp,name='addemp.html'),
     path('signup',views.signup,name='signup.html'),
     path('signin',views.signin,name='signin.html'),
     path('userhome',views.userhome,name='userhome.html'),
     path('signuppage',views.signuppage,name='signuppage'),
     path('signinpage',views.signinpage,name='signinpage'),
     path('signout',views.signout,name='signout'),
     path('insertEmp',views.insertEmp,name='insertEmp'),
     path('getEmp',views.getEmp,name='getEmp'),
     path('editEmp/<int:eid>',views.editEmp,name="editEmp"),
     path('updateEmp/<int:eid>',views.updateEmp,name="updateEmp"),
     path('deleteEmp/<int:eid>',views.deleteEmp,name="deleteEmp"),
    
]