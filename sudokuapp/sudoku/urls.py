from django.conf.urls import url
from .views import puzzle_element


urlpatterns = {
    url(r'^puzzle/{pk}/$', puzzle_element, name='puzzle'),
}
