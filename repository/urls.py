# repository/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduction, name='introduction'),
    path('home/', views.introduction, name='home'),
    # path('upload/', views.upload_material, name='upload_material'),
    path('detail/<int:id>/', views.material_detail, name='material_detail'),
    path('delete/<int:id>/', views.delete_material, name='delete_material'),
    path('first-page/', views.first_page, name='first_page'),
    path('second-page/', views.second_page, name='second_page'),
     path('edit-session/<int:id>/', views.edit_session, name='edit_session'), 
    # صفحات الأقسام مع البحث والرفع
    path('section1/', views.section1_page, name='section1_page'),
    path('section2/', views.section2_page, name='section2_page'),
    path('section3/', views.section3_page, name='section3_page'),
    
    # رفع البيانات لكل قسم
    path('upload-section1/', views.upload_section1, name='upload_section1'),
    path('upload-section2/', views.upload_section2, name='upload_section2'),
    path('upload-section3/', views.upload_section3, name='upload_section3'),
]