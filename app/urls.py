from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^profile/$',views.profile,name='prof'),
    # url('^profile/edit/$',views.edit_profile,name='edit'),
]