from django.contrib import admin
from django.urls import path  , include
from . import views
urlpatterns = [
   
    
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),

    path('home/',views.Home,name='home'),

    path('heart/', views.heart, name="heart"),
    # path('heart/heartsolution/', views.solution, name='solution'),
    # path('heart/congratulations/', views.congratulations, name='congratulations'),

    path("diabaties/", views.diabaties,name="diabaties"),
    path("diabaties/result/", views.result,name="result"),

    path('cancer', views.cancer, name="cancer"),
    # path('cancer/csolution/', views.cansolution, name='cansolution'),
    # path('cancer/congratulations/', views.cancongratulations, name='cancongratulations'),

    path('covid19', views.covid19, name="covid19"),
    # path('covid19/covidsolution/', views.covidsolution, name='covidsolution'),
    # path('covid19/congratulations/', views.covidcongratulations, name='covidcongratulations'),

    path('liver', views.liver, name="liver"),



    #PDF
    path('download_pdf/', views.download_pdfd, name='download_pdf'),
    path('download_pdf/', views.download_pdfh, name='download_pdf'),
    path('download_pdf/', views.download_pdfc, name='download_pdf'),
    path('download_pdf/', views.download_pdfco, name='download_pdf'),


    
]

