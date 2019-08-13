from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'profile/(?P<username>\w+)',views.profile,name='prof'),
    url('^profile/edit/$',views.edit_profile,name='edit'),
    url('^newhood',views.addneighbourhood,name="hood"),
]