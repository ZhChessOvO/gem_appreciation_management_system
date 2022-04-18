from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.page1, name='page1'),
    path('page1/add/', views.page1add, name='page1add'),
    path('page2/add/', views.page2add, name='page2add'),
    path('page2/edit/', views.page2edit, name='page2edit'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page3/edit/', views.page3edit, name='page3edit'),
    path('page4/', views.page4, name='page4'),
    path('page4/print/', views.page4print, name='page4print'),
    path('page4/delete/', views.page4delete, name='page4delete'),
    path('page5/', views.page5, name='page5'),
    path('page6/', views.page6, name='page6'),
    path('page6/add/', views.page6add, name='page6add'),
    path('page6/edit/', views.page6edit, name='page6edit'),
    path('page6/delete/', views.page6delete, name='page6delete'),
    path('page7/', views.page7, name='page7'),
    path('page8/', views.page8, name='page8'),
    # path('tables/', views.tables, name='tables'),
    # path('jumptest/',views.jumpTest,name='jumpTest'),
]
