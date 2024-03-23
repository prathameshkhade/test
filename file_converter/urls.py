from django.urls import path
from . import views

urlpatterns = [
    path('pdf_to_docx/', views.pdf_to_docx, name='pdf_to_docx'),
    path('download_file/', views.download_file, name='download_file'),
    path('pdf_to_ppt/', views.pdf_to_ppt, name='pdf_to_ppt'),
    path('pdf_to_excel/', views.pdf_to_excel, name='pdf_to_excel'),
    path('tables_to_excel/', views.tables_to_excel, name='tables_to_excel'),
    path('pdf_to_image/', views.pdf_to_image, name='pdf_to_image'),
    path('img_to_pdf/', views.img_to_pdf, name='img_to_pdf'),
    path('cleanup_temp_dir/', views.cleanup_temp_dir, name='cleanup_temp_dir'),
]
