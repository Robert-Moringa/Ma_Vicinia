from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^details/(\d+)', views.details, name='details'),
    url(r'^add/business/', views.addBusiness, name='business'),
    url(r'^add/health/', views.addHealth, name='health'),
    url(r'^add/police_post/', views.addPolice, name='police'),
    url(r'^business/(\d+)', views.business_details, name='business_details'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

