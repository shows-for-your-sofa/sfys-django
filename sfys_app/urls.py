from django.urls import include, path
from rest_framework import routers

from .views import EventViewSet, EventsView

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sfys', EventsView.as_view(), name='events'),
]
