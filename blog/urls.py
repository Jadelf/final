from django.conf.urls import url
from . import views

urlpatterns	=	[
				url(r'^$',	views.menu_list, name='menu_list'),
                url(r'^menu/(?P<pk>\d+)/$',	views.menu_detail,	name='menu_detail'),
                url(r'^new/$',	views.menu_new,	name='menu_new'),
]
