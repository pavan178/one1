from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^display_item1$', display_item1, name='display_item1'),
    url(r'^display_item2$', display_item2, name='display_item2'),
    url(r'^display_item3$', display_item3, name='display_item3'),

    url(r'^add_item1$', add_item1, name='add_item1'),
    url(r'^add_item2$', add_item2, name='add_item2'),
    url(r'^add_item3$', add_item3, name='add_item3'),

    url(r'^edit_item1/(?P<pk>\d+)$', edit_item1, name='edit_item1'),
    url(r'^edit_item2/(?P<pk>\d+)$', edit_item2, name='edit_item2'),
    url(r'^edit_item3/(?P<pk>\d+)$', edit_item3, name='edit_item3'),

    url(r'^delete_item1/(?P<pk>\d+)$', delete_item1, name='delete_item1'),
    url(r'^delete_item2/(?P<pk>\d+)$', delete_item2, name='delete_item2'),
    url(r'^delete_item3/(?P<pk>\d+)$', delete_item3, name='delete_item3'),

]
