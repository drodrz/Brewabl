from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

import allauth
from views import HomePage

from django.conf.urls import url, include
from rest_framework import routers
# from recipes.views import EventViewSet

# router = routers.DefaultRouter()
# router.register(r'event', EventViewSet)

urlpatterns = [
    url(r'^$', HomePage.as_view()),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
