from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('temp1/',views.temp1,name='temp1'),
    path('temp3/',views.temp3,name='temp3'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('temp2/',views.temp2,name='temp2'),
    path('generate-pdf2/', views.generate_pdf2, name='generate_pdf2'),
    path('generate_pdf3/', views.generate_pdf3, name='generate_pdf3'),
    
]
