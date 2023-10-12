from django.urls import path, include
from django.contrib import admin
from blogapp.views import home
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', home, name='home'),
    path('pages/', include('blogapp.urls')),
    path('messages/', include('messaging.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
