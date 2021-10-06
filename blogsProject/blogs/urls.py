from django.urls import path

from .views import *
urlpatterns=[
    path('',BlogsHomePageView.as_view(), name='home' ),


    path('post/<int:pk>/',BlogsDetailPageView.as_view(), name='post_details' ),
    path('post/new/',BlogsCreatePageView.as_view(), name='post_new' ),

    path('post/<int:pk>/edit/',BlogsUpdatePageView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/',BlogsDeletePageView.as_view(), name='post_remove' ),
]