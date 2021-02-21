from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("thanks/", views.thanks, name = "thanks"),
    path("analysis/", views.analysis, name = "analysis"),
    path("upload/", views.upload, name = "upload"),
    path("view-uploads/", views.view_uploads),
    path('download/<int:file_id>/', views.download),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
