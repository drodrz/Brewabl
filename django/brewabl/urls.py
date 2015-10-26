from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from rest_framework import routers
from accounts.views import UserViewSet, ProfileViewSet
from recipes.views import FermentableViewSet, HopViewSet, YeastViewSet, MiscViewSet, WaterProfileViewSet, \
    RecipeViewSet

router = routers.DefaultRouter()
router.register(r'fermentables', FermentableViewSet)
router.register(r'hops', HopViewSet)
router.register(r'yeast', YeastViewSet)
router.register(r'waterprofiles', MiscViewSet)
router.register(r'recipes', WaterProfileViewSet)
router.register(r'recipes', RecipeViewSet)

user_router = routers.DefaultRouter()
user_router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/', include(user_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
