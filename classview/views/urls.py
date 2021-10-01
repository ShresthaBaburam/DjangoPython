from django.urls import path
from .views import HomePageView,IndexPageView,ContactPageView

urlpatterns=[
    path('home/',HomePageView.as_view(), name='home'),
    path('',IndexPageView.as_view(), name='index'),
    path('contact',ContactPageView.as_view(), name='contact'),
]