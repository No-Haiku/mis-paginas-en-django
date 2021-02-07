from django.urls import path
from . import views

urlpatterns = [
    #path de page
    #path('',views.page, name="sample"),
    path('<int:page_id>/', views.page, name="page"),

    
]