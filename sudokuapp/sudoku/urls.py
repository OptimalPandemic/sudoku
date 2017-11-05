from django.conf.urls import url


urlpatters = {
    url(r'^puzzle/(?P<pk>[0-9]+)', 'puzzle_element'),
}