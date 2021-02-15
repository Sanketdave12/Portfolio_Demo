# Dave URL Configuration
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('', RedirectView.as_view(url="")),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
