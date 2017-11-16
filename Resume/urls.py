from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from ResumeA.views import index

urlpatterns = [
    url(r'^index/', index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
