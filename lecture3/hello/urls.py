from django.urls import path
from . import views

urlpatterns = [
  path("",views.index, name="index") ,
  path('<str:name>', views.greet, name="greet"),
  path('maziar',views.maziar,name="maziar"),
  path('aria',views.aria, name='aria'),
]