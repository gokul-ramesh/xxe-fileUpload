from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_xml, name='upload_xml'),
    path('display/<int:xml_id>/', views.display_xml, name='display_xml'),
]
