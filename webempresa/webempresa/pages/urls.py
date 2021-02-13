from django.urls import path
from . import views

urlpatterns = [
    #path de page
    #path('',views.page, name="sample"),
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),

    
]