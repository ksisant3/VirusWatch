from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name = "home"),
    path("<int:id>", views.index, name = "index"),
    path("home/", views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("thanks/", views.thanks, name = "thanks"),
    path("upload/", views.upload, name = "upload"),
    path("view-uploads/", views.view_uploads),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)