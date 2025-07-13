from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # For login, logout, password management
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #media files (like uploaded images) won’t be accessible through the browser in development.used only in development to serve media files (like images, PDFs, or uploaded documents) through Django's built-in development server
