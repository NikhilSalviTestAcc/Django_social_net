from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = 'index'),
    path('signup/',views.signup, name= 'signup'),
    path('signin/',views.signin, name= 'signin'),
    path('logout/',views.logout, name= 'logout'),
    path('settings/',views.settings, name= 'settings'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)