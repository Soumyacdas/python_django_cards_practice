from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='home'), 
    path('descriptions/', views.job_description,name='descriptions'), 
    path('details/', views.personal_details,name='details'), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)