from django.urls import path
from . import views 

urlpatterns = [ 
    path("",views.RegisterView.as_view()),
    path("/password",views.ChangePW.as_view()),


]