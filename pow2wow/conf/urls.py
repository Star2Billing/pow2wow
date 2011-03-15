from django.conf.urls.defaults import *
from conf.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( '',
    url( r'^$', index, name = 'conf_index' ),
    url( r'^(\d+)/$', member, name = 'conf_member' ),
    url( r'^(\d+)/kick/(\d+)/$', kick, name = 'action_kick' ),
    url( r'^(\d+)/kickall/$', kickall, name = 'action_kickall' ),
    url( r'^(\d+)/mute/(\d+)/$', mute, name = 'action_mute' ),
    url( r'^(\d+)/unmute/(\d+)/$', unmute, name = 'action_unmute' ),
    url( r'^(\d+)/member_refresh/$', member_refresh, name = 'member_refresh' ),

)
