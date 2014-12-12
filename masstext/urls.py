from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from masstext import views

urlpatterns = patterns('',

	# GET REQUESTS
    # /api/
    url(r'^$', views.index, name='index'),
    # /api/get/user/[api_key]
    url(r'^get/user/(?P<apiKey>\w+)/$', views.getUser, name='getUser'),
    # /api/get/members/[api_key]
    url(r'^get/members/(?P<apiKey>\w+)/$', views.getMembers, name='getMembers'),
    # /api/get/archived/[api_key]
    url(r'^get/archived/(?P<apiKey>\w+)/$', views.getArchived, name='getArchived'),
    # /api/get/unarchived/[api_key]
    url(r'^get/unarchived/(?P<apiKey>\w+)/$', views.getUnarchived, name='getUnarchived'),
    # /api/get/read/[api_key]
    url(r'^get/read/(?P<apiKey>\w+)/$', views.getRead, name='getRead'),
    # /api/get/unread/[api_key]
    url(r'^get/unread/(?P<apiKey>\w+)/$', views.getUnread, name='getUnread'),
    # /api/get/starred/[api_key]
    url(r'^get/starred/(?P<apiKey>\w+)/$', views.getStarred, name='getStarred'),
    # /api/get/unstarred/[api_key]
    url(r'^get/unstarred/(?P<apiKey>\w+)/$', views.getUnstarred, name='getUnstarred'),
    # /api/get/messages/[thread.id]/[api_key]
    url(r'^get/messages/(?P<threadId>\d+)/(?P<apiKey>\w+)/$', views.getMessages, name='getMessages'),
	
	# POST REQUESTS
    # /polls/post/send/[member.id]/[api_key]
    url(r'^post/send/(?P<memberId>\d+)/(?P<apiKey>\w+)/$', views.sendMessage, name='sendMessage'),
    # /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)