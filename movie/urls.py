from django.urls import path, include
from . import views
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('anime-tamil-dubbed', views.anime, name='anime'),
    path('kamal-haasan', views.Kamal, name='kamal_haasan'),
    path('vikram', views.vikram, name='vikram'),
    path('dhanush', views.dhanush, name='dhanush'),
    path('vijay-sethupathi', views.vijay_sethupathi, name='vijay-sethupathi'),
    # path('rajnikanth', views.rajnikanth, name='Rajnikanth'),
    path('suriya-sivakumar', views.suriya, name='suriya_sivakumar'),
    # path('joseph_vijay', views.joseph_vijay, name='Joseph_Vijay'),
    # path('ajith_kumar', views.ajith_kumar, name='Ajith_Kumar'),
    # path('vishal_krishna', views.vishal_krishna, name='Vishal_Krishna'),
    # path('fahadh_faasil', views.fahadh_faasil, name='Fahadh_Faasil'),
    # path('mahesh_babu', views.mahesh_babu, name='Mahesh_Babu'),
    # path('allu_arjun', views.allu_arjun, name='Allu_Arjun'),
    # path('prabhas', views.prabhas, name='Prabhas'),
    # path('ram_charan', views.ram_charan, name='Ram_Charan'),
    # path('jr_ntr', views.jr_ntr, name='Jr_NTR'),
    # path('ravi_teja', views.ravi_teja, name='Ravi_Teja'),
    # path('rana_daggubati', views.rana_daggubati, name='Rana_Daggubati'),
    # path('nani', views.nani, name='Nani'),
    # path('vijay_deverakonda', views.vijay_deverakonda, name='Vijay_Deverakonda'),
    path('<slug>', views.blog_detail, name='blog_detail'),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()