from django.urls import path
from .views import HomePageViews,SampleClassViews

urlpatterns = [
    path('', HomePageViews.as_view(), name="home"),
    path('sample/', SampleClassViews.as_view(), name="sample"),
]