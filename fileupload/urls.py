from django.contrib import admin
from django.urls import path
from main.views import FileSave, ListFiles
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filesave/', FileSave.as_view()),
    path('listfiles/', ListFiles.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)